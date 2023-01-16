import java.util.Arrays;

public class MultiDimensionArray {
    public static void main(String[] args) {
        // 每一子数组长度可以不相同
        int[][] ns = { { 1, 2, 3, 4 }, { 2, 3, 4, 5 }, { 3, 4, 5, 6, 1, 1, 1, 1, 1, 1, }, };
        System.out.println(Arrays.deepToString(ns));
    }
}