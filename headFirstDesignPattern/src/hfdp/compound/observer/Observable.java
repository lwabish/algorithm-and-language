package hfdp.compound.observer;

import java.util.ArrayList;
import java.util.Iterator;

/**
 * 所有被观察类都需要实现QuackObservable接口，所以弄一个公共的
 *
 * @author Lwabish
 */
public class Observable implements QuackObservable {

    ArrayList<Observer> observers = new ArrayList<>();
    QuackObservable duck;

    public Observable(QuackObservable duck) {
        this.duck = duck;
    }


    @Override
    public void registerObservers(Observer observer) {
        observers.add(observer);
    }

    @Override
    public void notifyObservers() {
        Iterator<Observer> iterator = observers.iterator();
        while (iterator.hasNext()) {
            Observer observer = iterator.next();
            observer.update(duck);
        }
    }
}
