package hfdp.command;

import hfdp.command.command.Command;
import hfdp.command.command.NoCommand;

import java.util.Arrays;

/**
 * @author Lwabish
 */
public class RemoteControl {
    Command[] onCommands;
    Command[] offCommands;

    public RemoteControl() {
        int amount = 7;
        onCommands = new Command[amount];
        offCommands = new Command[amount];

        Command noCommand = new NoCommand();
        for (int i = 0; i < amount; i++) {
            onCommands[i] = noCommand;
            offCommands[i] = noCommand;
        }
    }

    public void setCommand(int slot, Command on, Command off) {
        onCommands[slot] = on;
        offCommands[slot] = off;
    }

    public void onButtonPushed(int slot) {
        onCommands[slot].execute();
    }

    public void offButtonPushed(int slot) {
        offCommands[slot].execute();
    }

    @Override
    public String toString() {
        return "RemoteControl{" +
                "onCommands=" + Arrays.toString(onCommands) +
                ", offCommands=" + Arrays.toString(offCommands) +
                '}';
    }
}
