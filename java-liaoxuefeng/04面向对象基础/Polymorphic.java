public class Polymorphic extends Daddy1 {
    // 函数签名和父类一致：覆写（override）
    @Override // 希望编译器检查方法覆写，是否函数名、参数、返回值完全一致
    public void run(String x, String y) {

    }
    // 多态：父类定义好方法，子类只需要覆写实现即可，不需要修改父类的代码

}

class Daddy1 {
    protected String name;
    // final 属性不可被二次修改
    public final String onlyProperty = "";

    // 覆写object
    @Override
    public String toString() {
        return "daddy:" + name;
    }

    public void run(String x, String y) {

    }

    // final 禁止覆写
    public final void onlyVersion() {

    }
}

// final 类不允许被继承
final class onlyDaddy {

}