package hfdp.compound.compose;

import hfdp.compound.Quackable;
import hfdp.compound.observer.Observer;

import java.util.ArrayList;
import java.util.Iterator;

/**
 * @author Lwabish
 */
public class Flock implements Quackable {
    ArrayList<Quackable> quackables = new ArrayList<>();

    public void add(Quackable q) {
        quackables.add(q);
    }

    @Override
    public void quack() {
        Iterator<Quackable> iterator = quackables.iterator();
        while (iterator.hasNext()) {
            Quackable q = iterator.next();
            q.quack();
        }
    }

    @Override
    public void registerObservers(Observer observer) {
        for (Quackable q : quackables) {
            q.registerObservers(observer);
        }
    }

    @Override
    public void notifyObservers() {
        // flock里的每个duck在quack后会自己调用自己的notifyObservers，不需要这个公共的
    }
}
