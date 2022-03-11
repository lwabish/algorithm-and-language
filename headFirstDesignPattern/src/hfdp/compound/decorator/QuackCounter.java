package hfdp.compound.decorator;

import hfdp.compound.Quackable;
import hfdp.compound.observer.Observer;

/**
 * @author Lwabish
 */
public class QuackCounter implements Quackable {

    Quackable duck;
    static int number;

    public static int getNumber() {
        return number;
    }

    public QuackCounter(Quackable duck) {
        this.duck = duck;
    }


    @Override
    public void quack() {
        duck.quack();
        number += 1;
    }

    @Override
    public void registerObservers(Observer observer) {
        duck.registerObservers(observer);
    }

    @Override
    public void notifyObservers() {
        duck.notifyObservers();
    }
}
