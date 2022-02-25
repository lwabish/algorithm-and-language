package hfdp.singleton;

/**
 * java的单例
 *
 * @author Lwabish
 */
public class Singleton {

    private volatile static Singleton uniqueInstance;

    private String data;

    private Singleton() {
        data = "";
    }

    public String getData() {
        return data;
    }

    public void setData(String d) {
        data = d;
    }

    /**
     * 获取全局唯一的单例实例
     *
     * @return Singleton对象
     */
    public static Singleton getInstance() {
        // 一旦创建过对象，这里大多数情况是false，不需要加锁，直接走return逻辑
        if (uniqueInstance == null) {
            // 只有在单例对象初始化之前，不能容忍多线程
            // 因为这时可能创建出多个对象
            // 所以需要对实际初始化过程加锁，不需要对整个方法加锁
            // https://www.cnblogs.com/xz816111/p/8470048.html
            synchronized (Singleton.class) {
                if (uniqueInstance == null) {
                    uniqueInstance = new Singleton();
                }
            }
        }
        return uniqueInstance;
    }
}
