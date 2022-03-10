package hfdp.proxy.machine.states;

import hfdp.proxy.machine.GumballMachine;

/**
 * @author Lwabish
 */
public class WinnerState implements State {

    transient GumballMachine gumballMachine;

    public WinnerState(GumballMachine gumballMachine) {
        this.gumballMachine = gumballMachine;
    }

    @Override
    public void insertQuarter() {
        System.out.println("quarter not needed");
    }

    @Override
    public void ejectQuarter() {
        System.out.println("quarter has already been used");
    }

    @Override
    public void turnCrank() {
        System.out.println("crank already turned");
    }

    @Override
    public void dispense() {
        System.out.println("winner");
        gumballMachine.releaseBall();
        if (gumballMachine.getCount() > 0) {
            gumballMachine.releaseBall();
            if (gumballMachine.getCount() == 0) {
                gumballMachine.setState(gumballMachine.getSoldOutState());
            } else {
                gumballMachine.setState(gumballMachine.getNoQuarterState());
            }
        } else {
            gumballMachine.setState(gumballMachine.getSoldOutState());
        }
    }
}
