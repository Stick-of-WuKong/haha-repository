import java.io.FileInputStream;
import java.io.InputStream;
import java.io.ObjectInputStream;

public class Main {
    public static <Person> void main(String[] args) {

//        System.out.println("Hello world!");
        try {
            InputStream in = new FileInputStream("D:\\Document\\IDEAProjects\\TEST\\src\\jenkins_poc.ser");
            ObjectInputStream os = new ObjectInputStream(in);
            Person p2 = (Person)os.readObject();
            System.out.println(p2);
            os.close();
        }catch(Exception e) {
            e.printStackTrace();
        }
    }
}