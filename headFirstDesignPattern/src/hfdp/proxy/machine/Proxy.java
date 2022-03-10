package hfdp.proxy.machine;

import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;

/**
 * @author Lwabish
 */
public class Proxy {
    public static void main(String[] args) {
        try {
            GumballMachineRemote machine = (GumballMachineRemote) Naming.lookup("");
            Client client = new Client(machine);
            client.report();
        } catch (RemoteException | MalformedURLException | NotBoundException e) {
            e.printStackTrace();
        }
    }
}
