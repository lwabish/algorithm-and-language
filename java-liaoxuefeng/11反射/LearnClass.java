public class LearnClass {
    public static void main(String[] args) throws Exception {
        // 获取一个类的Class实例，该Class的实例由jvm创建，且和类一一对应，唯一
        // 方法1:
        Class<String> class1 = String.class;

        // 方法2：
        String s = "hello";
        Class<?> class2 = s.getClass();

        // 方法3：
        Class<?> class3 = Class.forName("java.lang.String");

        // 验证三个class是同一个
        System.out.println(class1 == class2);
        System.out.println(class1 == class3);

        printClassInfo("cls".getClass());
        printClassInfo(Runnable.class);
        printClassInfo(java.time.Month.class);
        printClassInfo(String[].class);
        printClassInfo(int.class);

        // 通过class实例构造类的实例
        // 局限：只能调用无参public构造方法
        // String s1 = (String) String.class.newInstance();
        // System.out.println(s1);
    }

    static void printClassInfo(Class<?> cls) {
        System.out.println("Class name: " + cls.getName());
        System.out.println("Simple name: " + cls.getSimpleName());
        if (cls.getPackage() != null) {
            System.out.println("Package name: " + cls.getPackage().getName());
        }
        System.out.println("is interface: " + cls.isInterface());
        System.out.println("is enum: " + cls.isEnum());
        System.out.println("is array: " + cls.isArray());
        // 八个基本类型
        System.out.println("is primitive: " + cls.isPrimitive());
        System.out.println();
    }
}
