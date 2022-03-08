package hfdp.iterator.recursive;

import hfdp.iterator.composition.MenuComponent;

import java.util.ArrayList;
import java.util.Iterator;

/**
 * @author Lwabish
 */
public class Menu extends MenuComponent {

    ArrayList<MenuComponent> menuComponents = new ArrayList<>();
    String name;
    String description;


    public Menu(String name, String description) {
        this.name = name;
        this.description = description;
    }

    /**
     * 递归方案中新增的方法
     * 如果是menu，就返回一个迭代器继续迭代子元素
     *
     * @return Iterator<MenuComponent>
     */
    @Override
    public Iterator<MenuComponent> createIterator() {
        return new CompositeIterator(menuComponents.iterator());
    }


    @Override
    public String getName() {
        return name;
    }

    @Override
    public String getDescription() {
        return description;
    }

    @Override
    public void print() {
        System.out.println(name);
        System.out.println(description);

        for (MenuComponent menuComponent : menuComponents) {
            menuComponent.print();
        }
    }

    @Override
    public void add(MenuComponent menuComponent) {
        menuComponents.add(menuComponent);
    }

    @Override
    public void remove(MenuComponent menuComponent) {
        menuComponents.remove(menuComponent);
    }

    @Override
    public MenuComponent getChild(int i) {
        return menuComponents.get(i);
    }

}
