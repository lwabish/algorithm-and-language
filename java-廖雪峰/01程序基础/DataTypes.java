public class DataTypes {
    /**
     * doc注释
     * 
     * @param args
     */
    public static void main(String[] args) {
        /**
         * 多行注释
         */
    }

    public static void basicTypes() {
        // java的整型均为有符号整数，最高位1表示负数
        // 整型 byte（1）-128 ~ 127
        byte iByte = 100;
        // 整型 short (2) -32768 ~ 32767
        short iShort = 10000;
        // 整型 int (4) -2147483648 ~ 2147483647
        int iInt = 10000000;
        // 整型 long (8) -9223372036854775808 ~ 9223372036854775807
        long iLong = 10000000000L;

        // 浮点 float (4)
        float f1 = 1.23f;
        float f2 = 1.23e1f;
        // 浮点 double (8)
        double d1 = 1.23;
        double d2 = 1.23e1;

        // 布尔 boolean (4)
        boolean b1 = true;
        boolean b2 = false;

        // 字符 char (2)
        char c1 = 'a';
        char c2 = '中';

    }

    public static void citedType() {
        String s1 = "哈哈哈";
        // 其他除基本类型以外的变量均为引用类型

        // 类型推导var
        var s2 = "abcde";

        // 常量
        final float PI = 1.23f;

    }
}