package hfdp.proxy.machine.states;

import java.io.Serializable;

/**
 * @author Lwabish
 */
public interface State extends Serializable {
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
