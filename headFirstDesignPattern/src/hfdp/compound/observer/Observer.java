package hfdp.compound.observer;

/**
 * @author Lwabish
 */
public interface Observer {

    /**
     * 被观察对象触发事件后调用
     *
     * @param duck 叫了的鸭子
     */
    void update(QuackObservable duck);
}
