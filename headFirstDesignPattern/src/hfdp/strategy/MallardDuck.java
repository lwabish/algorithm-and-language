package hfdp.strategy;

/**
 * @author wubowen
 */
public class MallardDuck extends Duck {
    @Override
    public void display() {
        System.out.println("\nI am a mallard duck");
    }

    /**
     * 绿头鸭 = 呱呱叫 + 会飞
     */
    public MallardDuck() {
        quackBehavior = new Quack();
        flyBehavior = new FlyWithWings();
    }
}
