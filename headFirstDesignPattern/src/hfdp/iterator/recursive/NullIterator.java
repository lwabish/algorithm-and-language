package hfdp.iterator.recursive;

import hfdp.iterator.composition.MenuComponent;

import java.util.Iterator;

/**
 * @author Lwabish
 */
public class NullIterator implements Iterator<MenuComponent> {
    @Override
    public boolean hasNext() {
        return false;
    }

    @Override
    public MenuComponent next() {
        return null;
    }

    @Override
    public void remove() {
        throw new UnsupportedOperationException();
    }
}
