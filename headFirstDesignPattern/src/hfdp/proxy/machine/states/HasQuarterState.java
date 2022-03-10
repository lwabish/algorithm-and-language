package hfdp.proxy.machine.states;

import hfdp.proxy.machine.GumballMachine;

import java.util.Random;

/**
 * @author Lwabish
 */
public class HasQuarterState implements State {

    transient GumballMachine gumballMachine;

    Random random = new Random(System.currentTimeMillis());

    public HasQuarterState(GumballMachine gumballMachine) {
        this.gumballMachine = gumballMachine;
    }

    @Override
    public void insertQuarter() {
        System.out.println("quarter not needed");
    }

    @Override
    public void ejectQuarter() {
        System.out.println("quarter ejected");
        gumballMachine.setState(gumballMachine.getNoQuarterState());
    }

    @Override
    public void turnCrank() {
        System.out.println("crank turned");
        int winner = random.nextInt(10);
        if (winner == 0 && gumballMachine.getCount() > 1) {
            gumballMachine.setState(gumballMachine.getWinnerState());
        } else {
            gumballMachine.setState(gumballMachine.getSoldState());
        }
    }

    @Override
    public void dispense() {
        System.out.println("turn crank first");
    }
}
