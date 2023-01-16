import java.lang.reflect.Field;
import java.lang.reflect.Modifier;

public class LearnField {
    public static void main(String[] args) throws Exception {
        Class<Student> stdClass = Student.class;
        // public
        System.out.println(stdClass.getField("score"));
        // public+继承
        System.out.println(stdClass.getField("name"));
        // private
        System.out.println(stdClass.getDeclaredField("grade"));

        Field f = String.class.getDeclaredField("value");
        System.out.println(f.getName());
        System.out.println(f.getType());
        int m = f.getModifiers();
        System.out.println(Modifier.isPublic(m));
        System.out.println(Modifier.isStatic(m));
        System.out.println(Modifier.isFinal(m));
        System.out.println(Modifier.isProtected(m));

        // 反射拿实例的值
        Object p = new Person("xiao ming");
        Class<?> c = p.getClass();
        Field field = c.getField("name");
        // 如果是private属性，需要先改为public
        field.setAccessible(true);
        System.out.println(field.get(p));

    }
}

class Person {
    public String name;

    public Person(String name) {
        this.name = name;
    }
}

class Student extends Person {
    public int score;
    private int grade;

    void nothing() {
        System.out.println(this.grade);
    }

    public Student(String name) {
        super(name);
    }
}