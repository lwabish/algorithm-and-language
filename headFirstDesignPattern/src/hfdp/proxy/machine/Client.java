package hfdp.proxy.machine;

import java.rmi.RemoteException;

/**
 * @author Lwabish
 */
public class Client {

    GumballMachineRemote gumballMachineRemote;

    public Client(GumballMachineRemote machineRemote) {
        this.gumballMachineRemote = machineRemote;
    }

    public void report() {
        try {
            System.out.println(gumballMachineRemote.getLocation());
            System.out.println(gumballMachineRemote.getState());
            System.out.println(gumballMachineRemote.getCount());
        } catch (RemoteException e) {
            e.printStackTrace();
        }
    }
}
