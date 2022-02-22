package hfdp.observer;

/**
 * @author wubowen
 */
public class WeatherStation {
    public static void main(String[] args) {
        // 初始化被观察者（Subject）
        WeatherData weatherData = new WeatherData();

        // 初始化观察者，开始订阅
        CurrentConditionsDisplay currentConditionsDisplay = new CurrentConditionsDisplay(weatherData);

        // 被订阅的主题发生变更
        weatherData.setMeasurements(1L, 2L, 3L);
        weatherData.setMeasurements(4L, 5L, 6L);

        // 观察者退出订阅
        currentConditionsDisplay.offline();

    }
}
