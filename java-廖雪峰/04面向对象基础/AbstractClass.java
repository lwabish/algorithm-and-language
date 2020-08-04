public class AbstractClass extends Daddy2 {
    // 必须实现父抽象类的抽象方法
    public void run(String x, byte y) {

    }

    public static void main(String[] args) {
        // 面向抽象编程
        Daddy2 d1 = new AbstractClass();
        // 抽象类调用不关心子类的具体实现
        d1.run("xxx", (byte) 1);
    }
}

// 抽象类
abstract class Daddy2 {
    // 抽象方法
    public abstract void run(String x, byte y);

    public void stop() {

    };

    protected String name;
}