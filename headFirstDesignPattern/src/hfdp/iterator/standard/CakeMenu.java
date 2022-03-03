package hfdp.iterator.standard;

import hfdp.iterator.handmade.MenuItem;

import java.util.ArrayList;
import java.util.Iterator;

/**
 * @author Lwabish
 */
public class CakeMenu implements Menu {

    ArrayList<MenuItem> menuItems;
    int position;

    public CakeMenu() {
        menuItems = new ArrayList<>();
        menuItems.add(new MenuItem("cake1", "cake1", false, 2.9));
        position = 0;
    }

    @Override
    public Iterator<MenuItem> createIterator() {
        return menuItems.iterator();
    }

}
