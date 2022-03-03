package hfdp.iterator.standard;

import hfdp.iterator.handmade.MenuItem;

import java.util.Iterator;

/**
 * @author Lwabish
 */
public class Waitress {
    Menu cakeMenu;
    Menu dinerMenu;

    public Waitress(CakeMenu cakeMenu, DinerMenu dinerMenu) {
        this.cakeMenu = cakeMenu;
        this.dinerMenu = dinerMenu;
    }

    public void printMenu() {
        // 省略了外部Iterator，直接把iterator写在了Menu类里
        printMenu(cakeMenu.createIterator());
        printMenu(dinerMenu.createIterator());
    }

    private void printMenu(Iterator iterator) {
        while (iterator.hasNext()) {
            MenuItem menuItem = (MenuItem) iterator.next();
            System.out.println(menuItem.getName());
        }
    }
}
