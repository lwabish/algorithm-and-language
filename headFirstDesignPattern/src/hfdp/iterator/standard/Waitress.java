package hfdp.iterator.standard;

import hfdp.iterator.handmade.MenuItem;

import java.util.Iterator;

/**
 * @author Lwabish
 */
public class Waitress {
    Menu cakeMenu;
    Menu dinerMenu;
    Menu cafeMenu;

    public Waitress(Menu cakeMenu, Menu dinerMenu, Menu cafeMenu) {
        this.cakeMenu = cakeMenu;
        this.dinerMenu = dinerMenu;
        this.cafeMenu = cafeMenu;
    }

    public void printMenu() {
        // 省略了外部Iterator，直接把iterator写在了Menu类里
        printMenu(cakeMenu.createIterator());
        printMenu(dinerMenu.createIterator());
        printMenu(cafeMenu.createIterator());
    }

    private void printMenu(Iterator<MenuItem> iterator) {
        while (iterator.hasNext()) {
            MenuItem menuItem = iterator.next();
            System.out.println(menuItem.getName());
        }
    }
}
