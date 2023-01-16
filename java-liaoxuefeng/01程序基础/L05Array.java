public class L05Array {
    public static void main(String[] args) {
        // 数组大小不可变
        int[] n = new int[5];
        // 数组字面量
        int[] m = new int[] { 1, 2, 3, 4, 5 };
        int[] o = { 1, 2, 3, 4, 5 };

        System.out.println(n.length);

        // 字符串数组
        String[] s = new String[] { "a", "b" };

        System.out.println(m);
        System.out.println(o);
        System.out.println(s);

        // 数组为不可变对象，修改会指向新创建的内存地址，原来的仍在内存中
        testArray();
    }

    // TODO: 分析内存存储结构
    static void testArray() {
        String[] names = { "A", "B", "C" };
        String s = names[0];
        names[0] = "X";
        // 同L04中对String做的测试结果类似，值仍然是A
        System.out.println(s);
    }
}