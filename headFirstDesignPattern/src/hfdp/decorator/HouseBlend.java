package hfdp.decorator;

/**
 * @author wubowen
 */
public class HouseBlend extends Beverage {

    /**
     * 饮料：综合咖啡
     */
    public HouseBlend() {
        description = "HouseBlend Coffee";
    }

    @Override
    public double cost() {
        return 0.89;
    }
}
