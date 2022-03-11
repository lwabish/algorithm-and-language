package hfdp.compound.factory;

import hfdp.compound.Quackable;

/**
 * @author Lwabish
 */
public abstract class AbstractGooseFactory {
    /**
     * 工厂函数
     *
     * @return 像鸭子的鹅
     */
    public abstract Quackable createGooseDuck();
}
