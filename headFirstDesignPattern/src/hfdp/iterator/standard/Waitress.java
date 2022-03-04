package hfdp.iterator.standard;

import hfdp.iterator.handmade.MenuItem;

import java.util.ArrayList;
import java.util.Iterator;

/**
 * @author Lwabish
 */
public class Waitress {
    ArrayList<Menu> menus;

    public Waitress(ArrayList<Menu> menus) {
        this.menus = menus;
    }

    public void printMenu() {
        menus.forEach(menu -> printMenu(menu.createIterator()));
    }

    private void printMenu(Iterator<MenuItem> iterator) {
        while (iterator.hasNext()) {
            MenuItem menuItem = iterator.next();
            System.out.println(menuItem.getName());
        }
    }
}
