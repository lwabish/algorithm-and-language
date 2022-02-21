package hfdp.strategy;

/**
 * @author wubowen
 */
public class ModelDuck extends Duck {
    @Override
    public void display() {
        System.out.println("\nI am a model duck");
    }

    public ModelDuck() {
        flyBehavior = new FlyNoWay();
        quackBehavior = new Quack();
    }
}
