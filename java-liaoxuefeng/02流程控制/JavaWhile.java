public class JavaWhile {
    public static void main(String[] args) {
        int sum = 0;
        int n = 0;
        while (n < 101) {
            sum += n;
            n++;
        }
        System.out.println(sum);

        int sum1 = 0;
        int n1 = 1;
        do {
            sum1 += n1;
            n1++;
        } while (n1 < 101);
        System.out.println(sum1);
    }
}