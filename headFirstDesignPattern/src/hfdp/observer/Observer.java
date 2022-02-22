package hfdp.observer;

/**
 * @author wubowen
 */
public interface Observer {

    /**
     * 当订阅主题的数据发生改变时，观察者对该接口的实现方法将被调用
     *
     * @param temp     温度
     * @param humidity 湿度
     * @param pressure 气压
     */
    void update(float temp, float humidity, float pressure);
}
