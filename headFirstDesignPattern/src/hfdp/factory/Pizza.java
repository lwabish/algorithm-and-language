package hfdp.factory;

import hfdp.factory.ingredient.Cheese;
import hfdp.factory.ingredient.Clams;
import hfdp.factory.ingredient.Dough;
import hfdp.factory.ingredient.Sauce;

/**
 * @author wubowen
 */
public abstract class Pizza {
    String name;

    /**
     * 面团类型
     */
    Dough dough;
    Sauce sauce;
    Cheese cheese;
    Clams clams;

    /**
     * 每种特定类型的pizza需要指定使用哪种原料工厂
     * 从而使用特定的一组原料（抽象工厂模式）
     */
    abstract void prepare();

    void bake() {
        System.out.println("baking for 25 minutes");
    }

    void cut() {
        System.out.println("cutting");
    }

    void box() {
        System.out.println("boxing");
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Pizza{" +
                "name='" + name + '\'' +
                ", dough=" + dough +
                ", sauce=" + sauce +
                ", cheese=" + cheese +
                ", clams=" + clams +
                '}';
    }
}
