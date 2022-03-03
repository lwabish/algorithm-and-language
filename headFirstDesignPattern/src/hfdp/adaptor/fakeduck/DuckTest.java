package hfdp.adaptor.fakeduck;

/**
 * @author Lwabish
 */
public class DuckTest {
    public static void main(String[] args) {
        testDuck(new TurKeyAdapter(new WildTurkey()));
    }

    private static void testDuck(Duck duck) {
        duck.quack();
        duck.fly();
    }
}
