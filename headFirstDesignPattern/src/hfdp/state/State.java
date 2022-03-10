package hfdp.state;

/**
 * @author Lwabish
 */
public interface State {
    /**
     * 1. 投硬币
     */
    void insertQuarter();

    /**
     * 2. 退硬币
     */
    void ejectQuarter();

    /**
     * 3. 转动曲柄
     */
    void turnCrank();

    /**
     * 4. 发放糖果
     */
    void dispense();
}
