package hfdp.compound.factory;

import hfdp.compound.Quackable;

/**
 * @author Lwabish
 */
public abstract class AbstractDuckFactory {

    /**
     * 工厂函数
     *
     * @return 鸭子
     */
    public abstract Quackable createMallardDuck();

    /**
     * 工厂函数
     *
     * @return 鸭子
     */
    public abstract Quackable createRedheadDuck();

    /**
     * 工厂函数
     *
     * @return 鸭子
     */
    public abstract Quackable createDuckCall();

    /**
     * 工厂函数
     *
     * @return 鸭子
     */
    public abstract Quackable createRubberDuck();
}
