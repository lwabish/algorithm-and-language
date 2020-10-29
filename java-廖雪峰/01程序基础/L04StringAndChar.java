public class L04StringAndChar {
    public static void main(String[] args) {
        char c1 = 'A';
        // char转Unicode码
        System.out.println((int) c1);
        // Unicode码转char
        System.out.println('\u1234');

        // 字符串拼接自动转换
        System.out.println("my age is " + 25);
        intToString();

        /**
         * java13后支持多行字符串，类似python。
         * 
         * 1.后面"""前的换行符也算作多行字符串的内容
         * 
         * 2.自动删前导空格，以最短行空格数为准
         * 
         * 3.编译时需要加入--source 14 --enable-preview
         */
        // String lonString = """
        // abcdefg
        // xxxxx
        // yyyy
        // ppppp
        // """;
        // System.out.println(lonString);

        // 字符串为不可变对象，和python一样
        // 同时字符串是引用类型变量，和python不一样
        // 分析变量的内存实际存储
        testString();

    }

    // TODO: 引用的本质？t=s这步的细节。
    static void testString() {
        String s = "hello";
        String t = s;
        s = "world";
        // t的值是hello，而不是world
        System.out.println(t);
    }

    static void intToString() {
        int a = 72;
        int b = 105;
        int c = 65281;

        // 正解：char转string：+""
        String s = "" + (char) a + (char) b + (char) c;
        System.out.println(s);

        // 特别注意：char和char的相加，是在做数值计算，而不是字符拼接
        System.out.println((char) a + (char) b);
    }
}