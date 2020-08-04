public class Array {
    public static void main(String[] args) {
        // 动态创建
        int[] n = new int[5];

        n[0] = 2;

        System.out.println(n[1]);

        n[0] = 3;

        System.out.println(n.length);

        // 数组字面量
        int[] m = new int[] { 1, 2, 3, 4, 5 };
        int[] o = { 1, 2, 3, 4, 5 };

        // 字符串数组
        String[] s = new String[] { "a", "b" };

        // 数组为不可变对象，修改会指向新创建的内存地址，原来的仍在内存中
    }
}