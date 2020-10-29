public class L02VarAndDataType {
    public static void main(String[] args) {
        // 只定义不初始化
        int x;
        x = 2;

        // 定义+初始化
        int y = 1;

        System.out.println(x);
        System.out.println(y);
        basicType();
        citedType();

        // 语句块与变量的作用域：变量仅在当前{}中存活
    }

    /**
     * java八种基本数据类型 四大类：整型，浮点，布尔，字符
     */
    static void basicType() {
        // java的整型均为有符号整数，最高位1表示负数
        // 可加下划线作为分节符方便肉眼区别
        // 整型 byte（1字节）-128 ~ 127
        byte iByte = 100;
        // 整型 short (2字节) -32768 ~ 32767
        short iShort = 10000;
        // 整型 int (4字节) -2147483648 ~ 2147483647
        int iInt = 10_000_000;
        // 整型 long (8字节) -9223372036854775808 ~ 9223372036854775807
        long iLong = 10000000000L;

        // 非十进制表示的整数
        int i1 = 0x12f;
        int i2 = 0b1001;

        // 浮点 float (4)
        float f1 = 1.23f;
        float f2 = 1.23e1f;
        // 浮点 double (8)
        double d1 = 1.23;
        double d2 = 1.23e1;

        // 布尔 boolean (根据oracle文档，布尔值的数据长度不确定，并非1byte或1bit。根据廖雪峰教程，jvm中常为4byte)
        boolean b1 = true;
        boolean b2 = false;

        // 字符 char (2)
        // 支持Ascii和Unicode
        // java内存中也是用Unicode存储字符
        char c1 = 'a';
        char c2 = '中';

        System.out.println("" + iByte + iShort + iInt + iLong + i1 + i2 + f1 + f2 + d1 + d2 + c1 + c2 + b1 + b2);

    }

    /**
     * 除8种基本类型以外的变量均为引用类型
     */
    static void citedType() {
        String s1 = "哈哈哈";

        // final 定义常量
        final float PI = 1.23f;

        // 类型推导var
        var s2 = "abcde";

        System.out.println(s1 + s2 + PI);

    }
}