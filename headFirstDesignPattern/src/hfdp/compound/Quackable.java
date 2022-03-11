package hfdp.compound;

import hfdp.compound.observer.QuackObservable;

/**
 * @author Lwabish
 */
public interface Quackable extends QuackObservable {

    /**
     * 叫
     */
    void quack();
}
