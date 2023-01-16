import java.util.Arrays;

public class Iterating {
    public static void main(String[] args) {
        int[] ar = { 1, 2, 3, 4, 5 };
        // for 遍历
        for (int i = 0; i < ar.length; i++) {
            System.out.println(ar[i]);
        }
        // for each遍历
        for (int i : ar) {
            System.out.println(i);
        }
        // Arrays.toString()方法
        System.out.println(Arrays.toString(ar));
    }

}