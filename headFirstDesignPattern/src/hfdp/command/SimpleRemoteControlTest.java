package hfdp.command;

import hfdp.command.command.Command;
import hfdp.command.command.LightOnCommand;
import hfdp.command.product.Light;

/**
 * @author Lwabish
 */
public class SimpleRemoteControlTest {
    public static void main(String[] args) {
        // 初始化一个灯
        Light light = new Light("撤所儿");

        // 用一个Command包装开灯的操作
        Command lightOnCommand = new LightOnCommand(light);

        // 初始化遥控器
        SimpleRemoteControl simpleRemoteControl = new SimpleRemoteControl();

        // 为遥控器设定操作的command
        simpleRemoteControl.setCommand(lightOnCommand);

        // 执行
        simpleRemoteControl.buttonWasPressed();
    }
}
