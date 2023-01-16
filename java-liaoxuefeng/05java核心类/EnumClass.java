public class EnumClass {
    public static void main(String[] args) {
        // enum不能被new出来，只能被定义后引用
        Weekday w1 = Weekday.MON;

        System.out.println(w1.name());
        System.out.println(w1.toString());
        System.out.println(w1.ordinal());

        // enum可以直接使用==比较，因为enum在内存中唯一
        if (w1.v == 1) {
            System.out.println("周一");
        }

        switch (w1) {
            case MON:
                System.out.println("MON");
            case TUE:
                System.out.println("TUE");
            default:
                System.out.println("other");
        }
    }
}

enum Weekday {
    MON(1, "星期一"), TUE(2, "星期二");

    public final int v;
    private final String t;

    private Weekday(int v, String t) {
        this.v = v;
        this.t = t;
    }

    @Override
    public String toString() {
        return this.t;
    }
}