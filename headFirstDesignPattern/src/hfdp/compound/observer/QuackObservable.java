package hfdp.compound.observer;

/**
 * @author Lwabish
 */
public interface QuackObservable {

    /**
     * 注册观察者
     *
     * @param observer 观察者
     */
    void registerObservers(Observer observer);

    /**
     * 通知观察者
     */
    void notifyObservers();
}
