import java.util.StringJoiner;

public class StringJoin {
    public static void main(String[] args) {
        String[] names = { "bob", "james", "marry" };
        StringJoiner sj = new StringJoiner(",", "hello,", "!");
        for (String name : names) {
            sj.add(name);
        }
        System.out.println(sj.toString());
        System.out.println(String.join(",", names));
    }
}