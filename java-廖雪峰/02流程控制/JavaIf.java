public class JavaIf {
    public static void main(String[] args) {

        int n = 50;
        if (n > 100) {
            System.out.println(">100");
        } else if (n > 60) {
            System.out.println("n>60");
        } else {
            System.out.println("other");
        }

        // 注意边界，注意顺序，浮点数判断不要用==
        // ==两侧为引用类型变量时，结果取决于引用对象是否是同一个

        // 判断字符串内容一样
        var s1 = "abc";
        var s2 = "abc";
        System.out.println(s1.equals(s2));

    }
}