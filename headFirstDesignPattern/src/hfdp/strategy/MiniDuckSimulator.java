package hfdp.strategy;

/**
 * @author wubowen
 */
public class MiniDuckSimulator {

    public static void main(String[] args) {
        Duck mallard = new MallardDuck();
        mallard.display();
        mallard.performQuack();
        mallard.performFly();
        mallard.swim();

        Duck model = new ModelDuck();
        model.display();
        model.performQuack();
        model.performFly();
        model.swim();

        model.display();
        // 动态改变行为
        model.setFlyBehavior(new FlyRocketPowered());
        model.performFly();
    }
}
