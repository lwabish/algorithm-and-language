package hfdp.iterator.standard;

import hfdp.iterator.handmade.MenuItem;

import java.util.HashMap;
import java.util.Iterator;

/**
 * @author Lwabish
 */
public class CafeMenu implements Menu {

    HashMap<String, MenuItem> menuItemHashMap = new HashMap<>();

    public CafeMenu() {
        menuItemHashMap.put("cafe1", new MenuItem("cafe1", "cafe1", true, 4.3));
    }

    @Override
    public Iterator<MenuItem> createIterator() {
        return menuItemHashMap.values().iterator();
    }
}
