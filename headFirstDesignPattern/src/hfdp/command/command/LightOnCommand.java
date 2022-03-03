package hfdp.command.command;

import hfdp.command.product.Light;

/**
 * @author Lwabish
 */
public class LightOnCommand implements Command {
    Light light;

    public LightOnCommand(Light light) {
        this.light = light;
    }

    @Override
    public void execute() {
        light.on();
    }
}
