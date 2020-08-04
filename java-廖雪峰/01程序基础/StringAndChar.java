public class StringAndChar {
    public static void main(String[] args) {
        // char对应Unicode字符集 2byte
        char c1 = 'A';
        // 查看unicode的十进制编码
        System.out.println((int) c1);
        // \\u表示法
        System.out.println('\u1234');

        // 字符串支持拼接
        // 字符串拼接自动转换
        System.out.println("my age is " + 25);
        /**
         * 支持多行字符串，类似python。 1.末尾'''如果前面有换行符，则会加入字符串内容 2.自动删前导空格，以最短行空格数为准
         * 3.编译时需要加入--source 14 --enable-preview
         */
        String lonString = """
                abcdefg
                xxxxx
                yyyy
                ppppp
                """;
        System.out.println(lonString);

        // 字符串为不可变对象，和python一样
        // 同时字符串是引用类型变量，和python不一样
        intToString();
    }

    public static void intToString() {
        int a = 72;
        int b = 105;
        int c = 65281;
        // char转string：+""
        String s = "" + (char) a + (char) b + (char) c;
        System.out.println(s);
    }
}