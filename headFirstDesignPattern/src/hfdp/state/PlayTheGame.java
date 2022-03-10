package hfdp.state;

/**
 * @author Lwabish
 */
public class PlayTheGame {
    public static void main(String[] args) {
        GumballMachine gumballMachine = new GumballMachine(50);
        int limit = 30;
        for (int i = 0; i < limit; i++) {
            play(gumballMachine);
        }
    }

    private static void play(GumballMachine gumballMachine) {
        System.out.println("----------");
        gumballMachine.insertQuarter();
        gumballMachine.ejectQuarter();
        gumballMachine.insertQuarter();
        gumballMachine.turnCrank();
    }
}
