package hfdp.state;

/**
 * @author Lwabish
 */
public class GumballMachine {

    //持有所有的状态实例

    State soldOutState;
    State noQuarterState;
    State hasQuarterState;
    State soldState;
    State winnerState;

    // 初始状态

    State state;
    int count;

    public GumballMachine(int number) {
        soldOutState = new SoldOutState(this);
        noQuarterState = new NoQuarterState(this);
        hasQuarterState = new HasQuarterState(this);
        soldState = new SoldState(this);
        winnerState = new WinnerState(this);
        count = number;
        if (number > 0) {
            state = noQuarterState;
        } else {
            state = soldOutState;
        }
    }

    // 接下来把机器的动作委托给状态类去做

    public void insertQuarter() {
        state.insertQuarter();
    }

    public void ejectQuarter() {
        state.ejectQuarter();
    }

    public void turnCrank() {
        state.turnCrank();
        state.dispense();
    }

    /**
     * 用来改变机器的状态
     */
    public void setState(State state) {
        this.state = state;
    }

    /**
     * 实际吐出糖果
     */
    void releaseBall() {
        System.out.println("ball released");
        if (count > 0) {
            count -= 1;
        }
    }

    public State getSoldOutState() {
        return soldOutState;
    }

    public State getNoQuarterState() {
        return noQuarterState;
    }

    public State getHasQuarterState() {
        return hasQuarterState;
    }

    public State getSoldState() {
        return soldState;
    }

    public int getCount() {
        return count;
    }

    public State getWinnerState() {
        return winnerState;
    }
}
