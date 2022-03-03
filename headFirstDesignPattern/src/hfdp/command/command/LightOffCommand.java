package hfdp.command.command;

import hfdp.command.product.Light;

/**
 * @author Lwabish
 */
public class LightOffCommand implements Command {

    Light light;

    public LightOffCommand(Light light) {
        this.light = light;
    }

    @Override
    public void execute() {
        light.off();
    }

}
