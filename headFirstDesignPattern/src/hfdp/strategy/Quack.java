package hfdp.strategy;

/**
 * @author wubowen
 */
public class Quack implements QuackBehavior {

    /**
     * 实现叫：呱呱叫
     */
    @Override
    public void quack() {
        System.out.println("Quack");
    }
}
