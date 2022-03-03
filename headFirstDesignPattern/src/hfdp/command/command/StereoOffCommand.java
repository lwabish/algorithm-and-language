package hfdp.command.command;

import hfdp.command.product.Stereo;

/**
 * @author Lwabish
 */
public class StereoOffCommand implements Command {

    Stereo stereo;

    public StereoOffCommand(Stereo stereo) {
        this.stereo = stereo;
    }

    @Override
    public void execute() {
        stereo.off();
    }
}
