public class Method {
    private String[] name;
    private int age;

    public static void main(String[] args) {
        // 基本类型调用传参：复制
        // 数组传参：传引用
        // String传参：传引用
    }

    public boolean setNames(String... names) {
        name = names;
        return true;
    }

    public boolean setAge(int age) {
        this.age = age;
        nothing();
        return true;
    }

    private void nothing() {
    }
}