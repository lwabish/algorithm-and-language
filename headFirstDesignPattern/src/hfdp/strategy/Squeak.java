package hfdp.strategy;

/**
 * @author wubowen
 */
public class Squeak implements QuackBehavior {

    /**
     * 实现叫：吱吱叫
     */
    @Override
    public void quack() {
        System.out.println("Squeak");
    }
}
