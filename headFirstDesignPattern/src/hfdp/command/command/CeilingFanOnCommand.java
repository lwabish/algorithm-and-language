package hfdp.command.command;

import hfdp.command.product.CeilingFan;

/**
 * @author Lwabish
 */
public class CeilingFanOnCommand implements Command {

    CeilingFan ceilingFan;
    int prevSpeed;

    public CeilingFanOnCommand(CeilingFan ceilingFan) {
        this.ceilingFan = ceilingFan;
    }

    @Override
    public void execute() {
        prevSpeed = ceilingFan.getSpeed();
        ceilingFan.medium();
    }

    @Override
    public void undo() {
        if (prevSpeed == CeilingFan.HIGH) {
            ceilingFan.high();
        } else if (prevSpeed == CeilingFan.MEDIUM) {
            ceilingFan.medium();
        } else if (prevSpeed == CeilingFan.LOW) {
            ceilingFan.low();
        } else {
            ceilingFan.off();
        }
    }
}
