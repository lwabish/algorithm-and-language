package hfdp.decorator;

/**
 * @author wubowen
 */
public class Whip extends CondimentDecorator {

    Beverage beverage;

    public Whip(Beverage b) {
        this.beverage = b;
    }

    @Override
    public double cost() {
        return 0.1 + beverage.cost();
    }

    @Override
    public String getDescription() {
        return beverage.getDescription() + " with whip";
    }
}
