package hfdp.decorator;

/**
 * @author wubowen
 */
public class Mocha extends CondimentDecorator {

    /**
     * 用一个成员变量记录其装饰的饮料，实现方法的链式调用
     */
    Beverage beverage;

    /**
     * 向饮料中加摩卡
     *
     * @param b 饮料
     */
    public Mocha(Beverage b) {
        // 装饰器的精髓：将被装饰者作为参数传入装饰器
        this.beverage = b;
    }

    @Override
    public double cost() {
        return 0.2 + beverage.cost();
    }

    @Override
    public String getDescription() {
        return beverage.getDescription() + " with mocha";
    }
}
