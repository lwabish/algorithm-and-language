package hfdp.observer;

/**
 * @author wubowen
 */
public interface Subject {

    /**
     * 注册
     *
     * @param o 观察者
     */
    void registerObserver(Observer o);

    /**
     * 移除
     *
     * @param o 观察者
     */
    void removeObserver(Observer o);

    /**
     * 通知
     */
    void notifyObservers();
}
