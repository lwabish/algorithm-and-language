package hfdp.observer;

import java.util.HashSet;
import java.util.Set;

/**
 * @author wubowen
 */
public class WeatherData implements Subject {

    /**
     * 改用set去重
     */
    private final Set<Observer> observers;

    private float temperature;
    private float humidity;
    private float pressure;

    public WeatherData() {
        observers = new HashSet<>();
    }

    @Override
    public void registerObserver(Observer o) {
        observers.add(o);
    }

    @Override
    public void removeObserver(Observer o) {
        observers.remove(o);
    }

    @Override
    public void notifyObservers() {
        observers.forEach(observer -> observer.update(temperature, humidity, pressure));
    }

    public void measurementChanged() {
        notifyObservers();
    }

    /**
     * 触发更新的起点在这里
     */
    public void setMeasurements(float t, float h, float p) {
        temperature = t;
        humidity = h;
        pressure = p;
        measurementChanged();
    }
}
