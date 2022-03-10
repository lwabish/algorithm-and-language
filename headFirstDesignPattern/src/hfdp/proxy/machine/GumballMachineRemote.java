package hfdp.proxy.machine;


import hfdp.proxy.machine.states.State;

import java.rmi.Remote;
import java.rmi.RemoteException;

/**
 * @author Lwabish
 */
public interface GumballMachineRemote extends Remote {
    /**
     * 获取机器剩余量
     *
     * @return 糖果机的剩余糖量
     * @throws RemoteException 远程错误
     */
    int getCount() throws RemoteException;

    /**
     * 获取机器地点
     *
     * @return 地点
     * @throws RemoteException 远程错误
     */
    String getLocation() throws RemoteException;

    /**
     * 获取机器状态
     *
     * @return 状态类
     * @throws RemoteException 远程错误
     */
    State getState() throws RemoteException;
}
