package hfdp.compound;

import hfdp.compound.compose.Flock;
import hfdp.compound.decorator.QuackCounter;
import hfdp.compound.factory.AbstractDuckFactory;
import hfdp.compound.factory.AbstractGooseFactory;
import hfdp.compound.factory.CountingDuckFactory;
import hfdp.compound.factory.GooseDuckFactory;
import hfdp.compound.observer.QuackObserver;

/**
 * @author Lwabish
 */
public class DuckSimulator {
    public static void main(String[] args) {
        DuckSimulator duckSimulator = new DuckSimulator();
        AbstractDuckFactory duckFactory = new CountingDuckFactory();
        AbstractGooseFactory gooseFactory = new GooseDuckFactory();
        duckSimulator.simulate(duckFactory, gooseFactory);
    }

    void simulate(AbstractDuckFactory duckFactory, AbstractGooseFactory gooseFactory) {
        Quackable mallardDuck = duckFactory.createMallardDuck();
        Quackable redheadDuck = duckFactory.createRedheadDuck();
        Quackable duckCall = duckFactory.createDuckCall();
        Quackable rubberDuck = duckFactory.createRubberDuck();

        Quackable gooseDuck = gooseFactory.createGooseDuck();

        Flock flock = new Flock();
        flock.add(mallardDuck);
        flock.add(redheadDuck);
        flock.add(duckCall);
        flock.add(rubberDuck);
        flock.add(gooseDuck);

        QuackObserver quackObserver = new QuackObserver();
        flock.registerObservers(quackObserver);

        simulate(flock);
        System.out.println("ducks quacked for " + QuackCounter.getNumber() + " times");

    }

    void simulate(Quackable quackable) {
        quackable.quack();
    }
}
