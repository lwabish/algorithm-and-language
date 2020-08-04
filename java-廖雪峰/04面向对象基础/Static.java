public class Static {
    public static String commonProperty = "0";

    public static void main(String[] args) {
        Static.commonProperty = "1";
        Static.test();
    }

    public static void test() {

    }
}

interface Final {
    // public static final
    int x = 1;

}