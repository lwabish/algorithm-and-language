package hfdp.compound;

import hfdp.compound.observer.Observable;
import hfdp.compound.observer.Observer;

/**
 * @author Lwabish
 */
public class DuckCall implements Quackable {

    Observable observable;

    public DuckCall() {
        observable = new Observable(this);
    }

    @Override
    public void quack() {
        System.out.println("kwak");
        notifyObservers();
    }

    @Override
    public void registerObservers(Observer observer) {
        observable.registerObservers(observer);
    }

    @Override
    public void notifyObservers() {
        observable.notifyObservers();
    }
}
