package hfdp.iterator.standard;

import hfdp.iterator.handmade.MenuItem;

import java.util.Iterator;

/**
 * @author Lwabish
 */
public class DinerMenu implements Menu {

    static final int MAX_ITEMS = 2;

    int position;

    MenuItem[] menuItems;

    public DinerMenu() {
        menuItems = new MenuItem[MAX_ITEMS];
        menuItems[0] = new MenuItem("diner1", "diner1", false, 1.0);
        menuItems[1] = new MenuItem("diner2", "diner2", false, 2.0);
        position = 0;
    }


    @Override
    public Iterator<MenuItem> createIterator() {
        return new DinerIterator(this.menuItems);
    }
}
