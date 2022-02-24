package hfdp.factory;

/**
 * @author Lwabish
 */
public abstract class PizzaStore {
    public Pizza orderPizza(String type) {
        Pizza pizza;

        pizza = createPizza(type);
        pizza.prepare();
        pizza.bake();
        pizza.cut();
        pizza.box();

        return pizza;
    }

    /**
     * 抽象类的实现类负责实际制作各自类型的pizza
     *
     * @param type 披萨类型
     * @return 披萨
     */
    abstract Pizza createPizza(String type);
}
