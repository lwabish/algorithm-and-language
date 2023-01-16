// 可以implement多个接口
public class Interface implements Person, Dog {
    public void run() {

    }

    public String getName() {
        return "";
    }

    public void eat() {

    }
}

// 接口：在抽象类的基础上，移除属性，只有方法
interface Person {
    // 默认public abstract，写了也白写
    void run();

    String getName();

    // 不需要实现
    default void live() {

    }
}

interface Dog {
    void eat();
}

// 接口可以继承接口，使用extends关键字
interface Bitch extends Dog {
    void fuckoff();
}