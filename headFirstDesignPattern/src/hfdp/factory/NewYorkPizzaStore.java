package hfdp.factory;

import hfdp.factory.ingredient.NewYorkPizzaIngredientFactory;
import hfdp.factory.ingredient.PizzaIngredientFactory;

/**
 * @author Lwabish
 */
public class NewYorkPizzaStore extends PizzaStore {


    @Override
    Pizza createPizza(String type) {
        Pizza pizza = null;

        PizzaIngredientFactory ingredientFactory = new NewYorkPizzaIngredientFactory();

        if (type != null) {
            pizza = new NewYorkPizza1(ingredientFactory);
            pizza.setName("pizza1");
        }

        return pizza;
    }
}
