package hfdp.decorator;

/**
 * @author wubowen
 */
public abstract class Beverage {
    String description = "Unknown Beverage";

    public String getDescription() {
        return description;
    }

    /**
     * 算价格
     *
     * @return 价格
     */
    public abstract double cost();
}
