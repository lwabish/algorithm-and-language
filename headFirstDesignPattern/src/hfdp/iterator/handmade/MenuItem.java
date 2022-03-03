package hfdp.iterator.handmade;

/**
 * @author Lwabish
 */
public class MenuItem {
    String name;

    String description;

    boolean veg;

    double price;

    public MenuItem(String name, String description, boolean veg, double price) {
        this.name = name;
        this.description = description;
        this.veg = veg;
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public String getDescription() {
        return description;
    }

    public boolean isVeg() {
        return veg;
    }

    public double getPrice() {
        return price;
    }
}
