public class L03Calculating {
    public static void main(String[] args) throws Exception {

        intCalculating();
        System.out.println();
        floatCalculating();
        System.out.println();
        boolCalculating();

    }

    static void intCalculating() throws Exception {
        // 整数除法结果为整数
        int x = 1000 / 7;
        System.out.println(x);
        // 除数为0时，可以编译，但是运行时报错
        // System.out.println(3 / 0);

        // 注意溢出问题
        // 转成二进制即可解释（最高位变成了1）
        System.out.println(2147483640 + 15);

        // 自运算
        // += -= *= /= ++ --
        int n = 100;
        // 先返回n，再对n++，打印结果为100，完成后n值为101
        System.out.println(n++);
        // 先对n++，再返回n，打印结果为102，完成后n值为102
        System.out.println(++n);

        // 整数的移位运算
        // 左移乘二，右移除二，注意移动导致的最高位变1问题，移动方向看尖朝哪儿
        // short和byte会先转成int再移位
        int m = 7;
        System.out.println(m << 1);
        System.out.println(m >> 1);

        // 无符号移位运算，只有右移，最高位永远为0
        int o = -1;
        System.out.println(o >>> 1);

        // 位运算符
        // 与
        n = 0 & 0;
        // 或
        n = 0 | 1;
        // 非
        n = ~0;
        // 异或，相异为1
        n = 0 ^ 1;

        /**
         * 运算符优先级
         * 
         * ()
         * 
         * ! ~ ++ --
         * 
         * * / %
         * 
         * + -
         * 
         * << >> >>>
         * 
         * &
         * 
         * |
         * 
         * += -= *= /=
         */

        // 小和大运算，小自动转换为大
        short s = 1234;
        int i = 123456;
        Object p = s + i;
        // s转为了int，p也是int
        System.out.println(p.getClass().getName());

        // 类型强转
        int i1 = 123456;
        // 强转会被截断
        short s1 = (short) i1;
        System.out.println(s1);

    }

    public static void floatCalculating() {
        // 关于浮点数，可以展开地非常深入，例
        // https://juejin.im/post/6860445359936798734
        // 简单讲：在实践中会影响浮点数的直接比较
        double x = 1.0 / 10;
        double y = 1 - 9.0 / 10;
        System.out.println(x);
        System.out.println(y);

        // 正确的浮点数比大小方法：
        double r = Math.abs(x - y);
        if (r < 0.00001) {
            System.out.println("equal");
        } else {
            System.out.println("not equal");
        }

        // 整数和浮点数运算，结果为浮点数
        int i2 = 5;
        Object d1 = 1.2 + 24.0 / i2;
        System.out.println(d1.getClass().getName());

        // 但是局部的整数与整数运算结果仍然为整数
        double d2 = 1.2 + 24 / i2;
        System.out.println(d2);

        // 特殊值
        // NaN
        System.out.println(0.0 / 0);
        // Infinity
        System.out.println(1.0 / 0);
        // -Infinity
        System.out.println(-1.0 / 0);

        // 浮点强转
        int i1 = (int) 12.3;
        // 一种对浮点数四舍五入的方法
        int i3 = (int) (12.3 + 0.5);
        System.out.println(i1);
        System.out.println(i3);
    }

    static void boolCalculating() {
        /**
         * 布尔运算符
         * 
         * > >= < <= == !=
         * 
         * && || !
         */

        // 短路运算，与python一致

        // 三元运算符，两个可能的返回值必须同类型
        int n = 1;
        int x = n > 0 ? n : -n;
        System.out.println(x);
    }
}