package hfdp.decorator;

/**
 * @author wubowen
 */
public class Espresso extends Beverage {

    /**
     * 饮料：浓缩咖啡
     */
    public Espresso() {
        description = "Espresso";
    }

    @Override
    public double cost() {
        return 1.99;
    }
}
