package hfdp.command.command;

import hfdp.command.product.GarageDoor;

/**
 * @author Lwabish
 */
public class GarageOnCommand implements Command {

    GarageDoor garageDoor;

    public GarageOnCommand(GarageDoor garageDoor) {
        this.garageDoor = garageDoor;
    }

    @Override
    public void execute() {
        garageDoor.lightOn();
        garageDoor.up();
    }

    @Override
    public void undo() {
        garageDoor.lightOff();
        garageDoor.down();
    }
}
