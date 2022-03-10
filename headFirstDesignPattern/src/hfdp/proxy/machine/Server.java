package hfdp.proxy.machine;

import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.RemoteException;

/**
 * @author Lwabish
 */
public class Server {
    public static void main(String[] args) {
        try {
            GumballMachineRemote gumballMachineRemote = new GumballMachine("bj", 10);

            Naming.rebind("rmi://localhost/machine1", gumballMachineRemote);
        } catch (RemoteException | MalformedURLException remoteException) {
            remoteException.printStackTrace();
        }

    }
}
