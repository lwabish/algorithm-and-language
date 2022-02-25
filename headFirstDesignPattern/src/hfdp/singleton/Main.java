package hfdp.singleton;

/**
 * @author Lwabish
 */
public class Main {
    public static void main(String[] args) {
        Singleton s1 = Singleton.getInstance();
        s1.setData("i am a singleton");
        Singleton s2 = Singleton.getInstance();
        System.out.println(s2.getData());

        System.out.println(s1 == s2);
    }
}
