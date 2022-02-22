package hfdp.observer;

/**
 * @author wubowen
 */
public class CurrentConditionsDisplay implements Observer, DisplayElement {

    private float temperature;
    private float humidity;
    private final Subject weatherData;

    public CurrentConditionsDisplay(Subject subject) {
        this.weatherData = subject;
        subject.registerObserver(this);
    }

    @Override
    public void display() {
        System.out.println("current temperature & humidity: " + temperature + "/" + humidity);
    }

    @Override
    public void update(float temp, float humidity, float pressure) {
        this.temperature = temp;
        this.humidity = humidity;
        display();
    }

    /**
     * 取消注册，不再订阅目标
     */
    public void offline() {
        this.weatherData.removeObserver(this);
    }
}
