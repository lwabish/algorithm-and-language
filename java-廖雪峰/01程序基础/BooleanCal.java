public class BooleanCal {
    public static void main(String[] args) {
        // > >= == !=

        // && || !

        // 短路运算，与python一致

        // 三元运算符，两个可能的返回值必须同类型
        int n = 1;
        int x = n > 0 ? n : -n;
        System.out.println(x);
    }
}