package hfdp.strategy;

/**
 * @author wubowen
 */
public class MuteQuack implements QuackBehavior {

    /**
     * 实现叫：不会叫
     */
    @Override
    public void quack() {
        System.out.println("<<Silence>>");
    }
}
