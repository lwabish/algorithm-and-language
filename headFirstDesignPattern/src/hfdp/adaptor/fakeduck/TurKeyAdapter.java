package hfdp.adaptor.fakeduck;

/**
 * @author Lwabish
 */
public class TurKeyAdapter implements Duck {
    Turkey turkey;

    public TurKeyAdapter(Turkey turkey) {
        this.turkey = turkey;
    }

    @Override
    public void quack() {
        turkey.gobble();
    }

    @Override
    public void fly() {
        turkey.fly();
        turkey.fly();
    }
}
