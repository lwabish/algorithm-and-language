import java.util.Scanner;

public class JavaIO {
    public static void main(String[] args) {
        System.out.println("");
        System.out.print("abc");
        // 占位符和python相似
        System.out.printf("%d\n", 19);
        input();
    }

    public static void input() {
        var s = new Scanner(System.in);
        var str = s.nextLine();
        var age = s.nextInt();
        System.out.printf("%s %d\n", str, age);

        s.close();
    }
}