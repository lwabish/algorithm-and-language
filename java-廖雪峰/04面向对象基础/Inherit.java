// 关键字extends
// 一个类只有一个父类，不允许多继承
public class Inherit extends Daddy {
    public int hello() {
        return age;
    }

    public static void main(String[] args) {
        System.out.println(x);

        // 向上转型：子类可以赋值给父类，反过来不可
        Inherit i = new Inherit();
        Daddy d = i;

        // instanceof
        System.out.println(i instanceof Inherit);
        System.out.println(i instanceof Daddy);

    }

    public Inherit() {
        // 因为父类没有无参构造函数，所以需要手动调用父类的构造函数。正常情况下编译器自动加super()
        super("abcd");
    }
}

class Daddy {
    // private无法被子类访问到
    private String name;
    // protected 可以被子类访问到
    protected int age;
    protected static int x;

    // 构造方法
    public Daddy(String x) {

    }

}