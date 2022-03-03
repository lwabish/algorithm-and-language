package hfdp.iterator.handmade;

/**
 * @author Lwabish
 */
public class DinerMenu implements Iterator {

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
    public boolean hasNext() {
        return position < menuItems.length;
    }

    @Override
    public Object next() {
        MenuItem menuItem = menuItems[position];
        position += 1;
        return menuItem;
    }
}
