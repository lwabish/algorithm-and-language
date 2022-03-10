package hfdp.state;

/**
 * @author Lwabish
 */
public class SoldOutState implements State {

    GumballMachine gumballMachine;

    public SoldOutState(GumballMachine gumballMachine) {
        this.gumballMachine = gumballMachine;
    }

    @Override
    public void insertQuarter() {
        System.out.println("sorry sold out");
    }

    @Override
    public void ejectQuarter() {
        System.out.println("no quarter to eject");
    }

    @Override
    public void turnCrank() {
        System.out.println("sold out sorry");
    }

    @Override
    public void dispense() {
        System.out.println("sold out sorry");
    }
}
