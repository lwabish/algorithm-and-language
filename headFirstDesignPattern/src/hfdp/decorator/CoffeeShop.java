package hfdp.decorator;

/**
 * @author wubowen
 */
public class CoffeeShop {
    public static void main(String[] args) {
        Beverage espresso = new Espresso();
        System.out.println(espresso.getDescription());
        System.out.println(espresso.cost());

        Beverage mixedBeverage = new Espresso();
        // 加点豆奶
        mixedBeverage = new Soy(mixedBeverage);
        // 加点whip
        mixedBeverage = new Whip(mixedBeverage);
        // 加点摩卡
        mixedBeverage = new Mocha(mixedBeverage);
        System.out.println(mixedBeverage.getDescription());
        System.out.println(mixedBeverage.cost());
    }
}
