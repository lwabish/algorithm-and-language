import java.util.Arrays;

public class Sorting {
    public static void main(String[] args) {
        var m = new int[] { 1, 2, 3 };
        var n = new String[] { "abc", "bcd", "efg" };
        // 对基本数据类型排序后，改变了实际位置
        Arrays.sort(m);
        // 对引用类型排序后，改变了指针
        Arrays.sort(n);
        System.out.println(m);
        System.out.println(n);

    }
}