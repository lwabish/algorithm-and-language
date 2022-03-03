package hfdp.iterator.handmade;

import java.util.ArrayList;

/**
 * @author Lwabish
 */
public class CakeMenu implements Iterator {

    ArrayList<MenuItem> menuItems;
    int position;

    public CakeMenu() {
        menuItems = new ArrayList<>();
        menuItems.add(new MenuItem("cake1", "cake1", false, 2.9));
        position = 0;
    }

    @Override
    public boolean hasNext() {
        return position < menuItems.size();
    }

    @Override
    public Object next() {
        MenuItem menuItem = menuItems.get(position);
        position += 1;
        return menuItem;
    }
}
