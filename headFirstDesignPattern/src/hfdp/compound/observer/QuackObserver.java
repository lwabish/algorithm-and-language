package hfdp.compound.observer;

/**
 * @author Lwabish
 */
public class QuackObserver implements Observer {
    @Override
    public void update(QuackObservable duck) {
        System.out.println("quack observed: " + duck);
    }
}
