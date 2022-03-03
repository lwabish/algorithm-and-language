package hfdp.command;

import hfdp.command.command.*;
import hfdp.command.product.CeilingFan;
import hfdp.command.product.GarageDoor;
import hfdp.command.product.Light;
import hfdp.command.product.Stereo;

/**
 * @author Lwabish
 */
public class RemoteControlTest {
    public static void main(String[] args) {
        RemoteControl remoteControl = new RemoteControl();

        // 初始化receiver，即实际执行命令的主体
        Light livingRoomLight = new Light("living room");
        Light kitchenLight = new Light("kitchen");
        CeilingFan ceilingFan = new CeilingFan("bathroom");
        GarageDoor garageDoor = new GarageDoor("street");
        Stereo stereo = new Stereo("street");

        // 初始化command，包裹命令执行主体
        LightOnCommand livingRoomLightOnCommand = new LightOnCommand(livingRoomLight);
        LightOffCommand livingRoomLightOffCommand = new LightOffCommand(livingRoomLight);
        LightOnCommand kitchenLightOnCommand = new LightOnCommand(kitchenLight);
        LightOffCommand kitchenLightOffCommand = new LightOffCommand(kitchenLight);
        CeilingFanOnCommand ceilingFanOnCommand = new CeilingFanOnCommand(ceilingFan);
        CeilingFanOffCommand ceilingFanOffCommand = new CeilingFanOffCommand(ceilingFan);
        GarageOnCommand garageOnCommand = new GarageOnCommand(garageDoor);
        GarageOffCommand garageOffCommand = new GarageOffCommand(garageDoor);
        StereoOnCommand stereoOnCommand = new StereoOnCommand(stereo);
        StereoOffCommand stereoOffCommand = new StereoOffCommand(stereo);

        // 给遥控器指定command
        remoteControl.setCommand(0, livingRoomLightOnCommand, livingRoomLightOffCommand);
        remoteControl.setCommand(1, kitchenLightOnCommand, kitchenLightOffCommand);
        remoteControl.setCommand(2, ceilingFanOnCommand, ceilingFanOffCommand);
        remoteControl.setCommand(3, garageOnCommand, garageOffCommand);
        remoteControl.setCommand(4, stereoOnCommand, stereoOffCommand);

        // 按遥控器开
        int slotCount = 5;
        for (int i = 0; i < slotCount; i++) {
            remoteControl.onButtonPushed(i);
        }

        // 按遥控器关
        for (int i = 0; i < slotCount; i++) {
            remoteControl.offButtonPushed(i);
        }

        System.out.println(remoteControl);

        // 测试undo按钮
        remoteControl.onButtonPushed(1);
        remoteControl.undoButtonPushed();


    }
}
