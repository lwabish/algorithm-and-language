package hfdp.iterator.recursive;

import hfdp.iterator.composition.MenuComponent;

import java.util.Iterator;

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

    /**
     * 下面是本包新增的功能
     */
    public void printVegetarianMenu() {
        Iterator<MenuComponent> iterator = parentMenu.createIterator();
        while (iterator.hasNext()) {
            MenuComponent menuComponent = iterator.next();
            try {
                if (menuComponent.isVegetarian()) {
                    menuComponent.print();
                }
            } catch (UnsupportedOperationException ignored) {
            }
        }
    }
}
