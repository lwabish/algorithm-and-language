package hfdp.factory.ingredient;

/**
 * @author Lwabish
 */
public interface PizzaIngredientFactory {

    /**
     * 生产饼皮
     *
     * @return 饼皮
     */
    Dough createDough();

    /**
     * 生产奶酪
     *
     * @return 奶酪
     */
    Cheese createCheese();

    /**
     * 生产酱汁
     *
     * @return 酱汁
     */
    Sauce createSauce();

    /**
     * 生产蛤蜊
     *
     * @return 蛤蜊
     */
    Clams createClams();

}
