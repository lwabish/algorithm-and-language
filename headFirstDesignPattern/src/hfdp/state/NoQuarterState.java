package hfdp.state;

/**
 * @author Lwabish
 */
public class NoQuarterState implements State {

    GumballMachine gumballMachine;

    public NoQuarterState(GumballMachine gumballMachine) {
        this.gumballMachine = gumballMachine;
    }

    @Override
    public void insertQuarter() {
        // 在NoQuarter状态下insertQuarter，会发生什么？
        System.out.println("quarter inserted");
        gumballMachine.setState(gumballMachine.getHasQuarterState());
    }

    @Override
    public void ejectQuarter() {
        System.out.println("no quarter to eject");
    }

    @Override
    public void turnCrank() {
        System.out.println("a quarter needed");
    }

    @Override
    public void dispense() {
        System.out.println("a quarter needed");
    }
}
