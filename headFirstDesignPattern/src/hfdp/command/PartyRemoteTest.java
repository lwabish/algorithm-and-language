package hfdp.command;

import hfdp.command.command.Command;
import hfdp.command.command.LightOffCommand;
import hfdp.command.command.LightOnCommand;
import hfdp.command.party.MacroCommand;
import hfdp.command.product.Light;

/**
 * @author Lwabish
 */
public class PartyRemoteTest {
    public static void main(String[] args) {
        Light livingRoomLight = new Light("living room");
        Light kitchenLight = new Light("kitchen");
        LightOnCommand livingRoomLightOnCommand = new LightOnCommand(livingRoomLight);
        LightOnCommand kitchenLightOnCommand = new LightOnCommand(kitchenLight);
        LightOffCommand livingRoomLightOffCommand = new LightOffCommand(livingRoomLight);
        LightOffCommand kitchenLightOffCommand = new LightOffCommand(kitchenLight);


        Command[] partyOn = {livingRoomLightOnCommand, kitchenLightOnCommand};
        Command[] partyDone = {livingRoomLightOffCommand, kitchenLightOffCommand};
        MacroCommand partyOnMacro = new MacroCommand(partyOn);
        MacroCommand partyDoneMacro = new MacroCommand(partyDone);

        RemoteControl remoteControl = new RemoteControl();
        remoteControl.setCommand(0, partyOnMacro, partyDoneMacro);

        remoteControl.onButtonPushed(0);
        remoteControl.offButtonPushed(0);
    }
}
