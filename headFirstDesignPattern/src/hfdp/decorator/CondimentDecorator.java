package hfdp.decorator;

/**
 * @author wubowen
 */
public abstract class CondimentDecorator extends Beverage {

    /**
     * 调料必须重新实现该方法
     *
     * @return 描述
     */
    @Override
    public abstract String getDescription();
}
