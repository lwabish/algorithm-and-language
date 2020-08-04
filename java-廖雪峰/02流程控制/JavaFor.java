public class JavaFor {

    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            System.out.println(i);
        }

        // for each
        int[] ns = { 1, 2, 3, 4 };
        for (int x : ns) {
            System.out.println(x);
        }
    }
}