package hfdp.iterator.composition;

/**
 * @author Lwabish
 */
public class Waitress {
    MenuComponent parentMenu;


    public Waitress(MenuComponent parentMenu) {
        this.parentMenu = parentMenu;
    }

    public void printMenu() {
        parentMenu.print();
    }
}
