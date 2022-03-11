package hfdp.compound;

import hfdp.compound.observer.Observable;
import hfdp.compound.observer.Observer;

/**
 * 绿头鸭
 *
 * @author Lwabish
 */
public class MallardDuck implements Quackable {

    Observable observable;

    public MallardDuck() {
        observable = new Observable(this);
    }

    @Override
    public void quack() {
        System.out.println("quack");
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
