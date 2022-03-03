package hfdp.command.command;

import hfdp.command.product.GarageDoor;

/**
 * @author Lwabish
 */
public class GarageOffCommand implements Command {

    GarageDoor garageDoor;

    public GarageOffCommand(GarageDoor garageDoor) {
        this.garageDoor = garageDoor;
    }

    @Override
    public void execute() {
        garageDoor.lightOff();
        garageDoor.down();
    }
}
