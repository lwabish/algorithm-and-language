package hfdp.factory;

/**
 * @author Lwabish
 */
public class OrderPizza {
    public static void main(String[] args) {
        // new york
        PizzaStore newyorkStore = new NewYorkPizzaStore();
        Pizza newyorkPizza = newyorkStore.orderPizza("whatever");
        System.out.println("a newyork pizza ordered: " + newyorkPizza);
    }
}
