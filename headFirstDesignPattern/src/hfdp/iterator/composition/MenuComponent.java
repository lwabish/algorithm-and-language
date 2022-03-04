package hfdp.iterator.composition;

/**
 * @author Lwabish
 */
public abstract class MenuComponent {
    /**
     * 以下是菜单和菜单项均需要重写的方法
     */

    public String getName() {
        throw new UnsupportedOperationException();
    }

    public String getDescription() {
        throw new UnsupportedOperationException();
    }

    public void print() {
        throw new UnsupportedOperationException();
    }


    /**
     * 以下是作为菜单需要重写的方法
     */

    public void add(MenuComponent menuComponent) {
        throw new UnsupportedOperationException();
    }

    public void remove(MenuComponent menuComponent) {
        throw new UnsupportedOperationException();
    }

    public MenuComponent getChild(int i) {
        throw new UnsupportedOperationException();
    }

    /**
     * 以下是作为菜单项需要重写的
     */

    public double getPrice() {
        throw new UnsupportedOperationException();
    }

    public boolean isVegetarian() {
        throw new UnsupportedOperationException();
    }
}
