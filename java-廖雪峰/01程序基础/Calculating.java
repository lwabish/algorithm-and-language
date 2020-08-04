public class Calculating {
    public static void main(String[] args) {
        // 整数除法结果为整数
        // 除数为0时，编译不报错，运行报错
        // 整数运算注意溢出问题
        int x = 1000 / 7;
        System.out.println(x);

        // 自增减运算法
        int n = 100;
        // 先返回n，再对n++，打印结果为100，完成后n值为101
        System.out.println(n++);
        // 先对n++，再返回n，打印结果为102，完成后n值为102
        System.out.println(++n);

        // 移位运算符
        // 左移乘二，右移除二，注意移动导致的最高位变1问题，移动方向看尖朝哪儿
        int m = 7;
        System.out.println(m << 1);
        System.out.println(m >> 1);

        // 无符号移位运算，只有右移，最高位永远为0
        int o = -1;
        System.out.println(o >>> 1);

        // 位运算符
        n = 0 & 0; // 与
        n = 0 | 1; // 或
        n = ~0; // 非
        n = 0 ^ 1; // 异或，相异为1

        // 类型自动转换
        short s = 1234;
        int i = 123456;
        // s自动转为int，结果p也为int
        int p = s + i;

        // 类型强转
        int i1 = 123456;
        // 强转会被截断
        short s1 = (short) i1;
        System.out.println(s1);

        floatCalculating();

    }

    public static void floatCalculating() {
        // 浮点数的不精确性
        double x = 1.0 / 10;
        double y = 1 - 9.0 / 10;
        System.out.println(x);
        System.out.println(y);

        // 浮点数比大小
        double r = Math.abs(x - y);
        if (r < 0.00001) {
            System.out.println("equal");
        } else {
            System.out.println("not equal");
        }

        // 整型的自动转换
        int i2 = 5;
        // 整数和浮点数运算，结果为浮点数
        double d1 = 1.2 + 24.0 / i2;
        System.out.println(d1);
        // 但是局部的整数与整数运算结果仍然为整数
        double d2 = 1.2 + 24 / i2;
        System.out.println(d2);

        // 浮点强转
        int i1 = (int) 12.3;
        // 四舍五入
        int i3 = (int) (12.3 + 0.5);
        System.out.println(i1);
        System.out.println(i3);
    }
}