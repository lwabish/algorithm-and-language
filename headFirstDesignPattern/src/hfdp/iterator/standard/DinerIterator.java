package hfdp.iterator.standard;

import hfdp.iterator.handmade.MenuItem;

import java.util.Iterator;

/**
 * @author Lwabish
 */
public class DinerIterator implements Iterator<MenuItem> {

    MenuItem[] menuItems;

    int position;

    public DinerIterator(MenuItem[] menuItems) {
        position = 0;
        this.menuItems = menuItems;
    }

    @Override
    public boolean hasNext() {
        return position < menuItems.length;
    }

    @Override
    public MenuItem next() {
        MenuItem menuItem = menuItems[position];
        position += 1;
        return menuItem;
    }
}
