package hfdp.proxy.machine;

import hfdp.proxy.machine.states.*;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

/**
 * @author Lwabish
 */
public class GumballMachine extends UnicastRemoteObject implements GumballMachineRemote {

    //持有所有的状态实例

    State soldOutState;
    State noQuarterState;
    State hasQuarterState;
    State soldState;
    State winnerState;

    // 初始状态

    State state;
    int count;
    String location;

    public GumballMachine(String location, int number) throws RemoteException {
        soldOutState = new SoldOutState(this);
        noQuarterState = new NoQuarterState(this);
        hasQuarterState = new HasQuarterState(this);
        soldState = new SoldState(this);
        winnerState = new WinnerState(this);
        count = number;
        this.location = location;
        if (number > 0) {
            state = noQuarterState;
        } else {
            state = soldOutState;
        }
    }

    // 接下来把机器的动作委托给状态类去做

    public void insertQuarter() {
        state.insertQuarter();
    }

    public void ejectQuarter() {
        state.ejectQuarter();
    }

    public void turnCrank() {
        state.turnCrank();
        state.dispense();
    }

    /**
     * 用来改变机器的状态
     */
    public void setState(State state) {
        this.state = state;
    }

    /**
     * 实际吐出糖果
     */
    public void releaseBall() {
        System.out.println("ball released");
        if (count > 0) {
            count -= 1;
        }
    }

    public State getSoldOutState() {
        return soldOutState;
    }

    public State getNoQuarterState() {
        return noQuarterState;
    }

    public State getHasQuarterState() {
        return hasQuarterState;
    }

    public State getSoldState() {
        return soldState;
    }

    @Override
    public int getCount() {
        return count;
    }

    @Override
    public String getLocation() throws RemoteException {
        return location;
    }

    @Override
    public State getState() throws RemoteException {
        return state;
    }

    public State getWinnerState() {
        return winnerState;
    }
}
