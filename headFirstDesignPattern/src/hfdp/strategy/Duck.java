package hfdp.strategy;

/**
 * @author wubowen
 */
public abstract class Duck {

    FlyBehavior flyBehavior;

    public void setFlyBehavior(FlyBehavior fb) {
        flyBehavior = fb;
    }

    QuackBehavior quackBehavior;

    public void setQuackBehavior(QuackBehavior qb) {
        quackBehavior = qb;
    }

    public Duck() {
    }

    /**
     * 显示鸭子的不同种类
     */
    public abstract void display();

    /**
     * 执行动作：飞
     */
    public void performFly() {
        flyBehavior.fly();
    }

    /**
     * 执行动作：叫
     */
    public void performQuack() {
        quackBehavior.quack();
    }

    /**
     * 执行动作：游泳
     */
    public void swim() {
        System.out.println("all ducks swim");
    }
}
