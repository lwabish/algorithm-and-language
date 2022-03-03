package hfdp.command.command;

import hfdp.command.product.Stereo;

/**
 * @author Lwabish
 */
public class StereoOnCommand implements Command {

    Stereo stereo;

    public StereoOnCommand(Stereo stereo) {
        this.stereo = stereo;
    }

    @Override
    public void execute() {
        stereo.setCd();
        stereo.on();
    }
}
