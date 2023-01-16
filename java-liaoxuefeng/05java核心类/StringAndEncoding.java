import java.nio.charset.StandardCharsets;
import java.util.Arrays;

public class StringAndEncoding {
    public static void main(String[] args) {
        // 字符串不可变
        String s1 = "Hello";
        s1 = s1.toUpperCase();
        System.out.println(s1);

        // 字符串相等判断：用equals
        String s2 = "hello";
        String s3 = "hello";
        String s4 = "HELLO".toLowerCase();
        System.out.println(s2.equals(s3));
        System.out.println(s2 == s3);
        System.out.println(s2.equals(s4));

        // 传数组导致的类私有属性意外改变
        int[] scores = { 1, 2, 3, 4, 5 };
        Score sc1 = new Score(scores);
        sc1.printScores();
        scores[0] = 100;
        sc1.printScores();

        // string和char数组的互转
        char[] cs = "hahaha".toCharArray();
        String s5 = new String(cs);
        System.out.println(s5);

        // 字符串编码：字符串-->byte[]
        byte[] b1 = "h".getBytes();
        // byte[] b2 = "h".getBytes("GBK");
        byte[] b4 = "h".getBytes(StandardCharsets.UTF_8);

        // 字符串解码：byte[]-->字符串
        String s6 = new String(b1, StandardCharsets.UTF_8);
        System.out.println(b1);
        System.out.println(s6);

    }
}

class Score {
    private int[] scores;

    public Score(int[] scores) {
        // 浅拷贝
        // this.scores = scores;

        // 深拷贝
        this.scores = scores.clone();
    }

    public void printScores() {
        System.out.println(Arrays.toString(scores));
    }
}