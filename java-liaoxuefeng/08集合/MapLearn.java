import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

public class MapLearn {
    public static void main(String[] args) {
        Student s = new Student("a", 99);
        Map<String, Student> map = new HashMap<>();
        map.put("a", s);

        Student target = map.get("a");

        // 同一个对象
        System.out.println(target == s);
        System.out.println(target.score);

        System.out.println(map.get("abcde"));

        // 遍历map----key
        Map<String, Integer> map1 = new HashMap<>();
        map1.put("1", 1);
        map1.put("2", 2);
        for (String key : map1.keySet()) {
            System.out.println(map1.get(key));
        }

        // 遍历map----entry
        for (Map.Entry entry : map1.entrySet()) {
            System.out.println("----");
            System.out.println(entry.getKey());
            System.out.println(entry.getValue());
        }

    }
}

class Student {
    String name;
    int score;

    Student(String name, int score) {
        this.name = name;
        this.score = score;
    }

    // 做key的要求1：equals方法
    public boolean equals(Object o) {
        if (o instanceof Student) {
            Student s = (Student) o;
            return Objects.equals(o.name, this.name) && this.score == o.score;
        }
        return false;
    }

    // 做key的要求2：hashCode方法
    public int hashCode() {
        int h = 0;
        h = 31 * h + name.hashCode();
        h = 31 * h + score;
        return h;
    }
}