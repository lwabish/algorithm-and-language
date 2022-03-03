package hfdp.template;

/**
 * @author Lwabish
 */
public abstract class CaffeineBeverageWithHook {

    /**
     * 这里是模板设计模式中的模板
     * 整个流程的公共部分被封装起来，并且禁止修改
     * 但是其中有些非公共部分，会定义成抽象方法由子类实现
     * 且加入了钩子，允许子类靠实现来影响流程控制
     */
    final void prepareRecipe() {
        boilWater();
        brew();
        pourInCup();
        if (needCondiments()) {
            addCondiments();
        }
    }

    /**
     * 这是一个钩子
     * 默认加调料
     * 可以覆写返回false不加
     */
    boolean needCondiments() {
        return true;
    }

    /**
     * 由具体饮品决定用何种工艺制作
     */
    abstract void brew();

    /**
     * 是否加调料
     */
    abstract void addCondiments();

    /**
     * 算法的公共部分
     */
    void boilWater() {
        System.out.println("boil water");
    }

    /**
     * 算法的公共部分
     */
    void pourInCup() {
        System.out.println("pour into cup");
    }


}
