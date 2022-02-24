package hfdp.factory;

import hfdp.factory.ingredient.PizzaIngredientFactory;

/**
 * @author Lwabish
 */
public class NewYorkPizza1 extends Pizza {
    PizzaIngredientFactory pizzaIngredientFactory;

    public NewYorkPizza1(PizzaIngredientFactory pizzaIngredientFactory) {
        this.pizzaIngredientFactory = pizzaIngredientFactory;
    }

    @Override
    void prepare() {
        cheese = pizzaIngredientFactory.createCheese();
        clams = pizzaIngredientFactory.createClams();
        dough = pizzaIngredientFactory.createDough();
        sauce = pizzaIngredientFactory.createSauce();
        System.out.println("prepared: " + this);
    }
}
