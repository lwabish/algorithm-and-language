package hfdp.command;

import hfdp.command.command.Command;

/**
 * @author Lwabish
 */
public class SimpleRemoteControl {
    Command slot;

    /**
     * 为什么不在构造方法里初始化？因为需要支持运行时更改
     *
     * @param command 命令
     */
    public void setCommand(Command command) {
        this.slot = command;
    }

    public void buttonWasPressed() {
        slot.execute();
    }
}
