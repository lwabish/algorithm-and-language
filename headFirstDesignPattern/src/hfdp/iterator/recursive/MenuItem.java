package hfdp.iterator.recursive;

import hfdp.iterator.composition.MenuComponent;

import java.util.Iterator;

/**
 * @author Lwabish
 */
public class MenuItem extends MenuComponent {

    String name;
    String description;
    boolean vegetarian;
    double price;

    public MenuItem(String name, String description, boolean vegetarian, double price) {
        this.name = name;
        this.description = description;
        this.vegetarian = vegetarian;
        this.price = price;
    }

    /**
     * 菜单项没有子菜单，无法继续迭代
     *
     * @return 空迭代器
     */
    @Override
    public Iterator<MenuComponent> createIterator() {
        return new NullIterator();
    }


    @Override
    public String getName() {
        return this.name;
    }

    @Override
    public String getDescription() {
        return this.description;
    }

    @Override
    public void print() {
        System.out.println(name + description + vegetarian + price);
    }

    @Override
    public double getPrice() {
        return this.price;
    }

    @Override
    public boolean isVegetarian() {
        return this.vegetarian;
    }
}
