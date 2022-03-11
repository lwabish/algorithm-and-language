package hfdp.compound.adapter;

import hfdp.compound.Quackable;
import hfdp.compound.observer.Observable;
import hfdp.compound.observer.Observer;

/**
 * @author Lwabish
 */
public class GooseAdapter implements Quackable {
    Observable observable;
    Goose goose;

    public GooseAdapter(Goose goose) {
        this.goose = goose;
        observable = new Observable(this);
    }

    @Override
    public void quack() {
        goose.honk();
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
