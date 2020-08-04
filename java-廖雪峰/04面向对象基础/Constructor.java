public class Constructor {
    // null
    private String name;
    // 0
    private int age;
    // 直接初始化赋值
    private int sex = 0;
    // 构造函数晚于初始化，所以终值为构造函数中修改的值

    public static void main(String[] args) {

    }

    // 构造函数：不写返回值，响应new操作符
    public Constructor(String x, int y) {
    }

    // 可以定义多个构造函数
    public Constructor(String z) {

    }

    // 构造方法的互调用
    public Constructor() {
        this("z");
    }
}