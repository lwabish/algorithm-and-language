import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class LearnLambda {
    public static void main(String[] args) {

        // 普通写法
        String[] arr = new String[] { "1", "2" };
        Arrays.sort(arr, new Comparator<String>() {
            public int compare(String s1, String s2) {
                return s1.compareTo(s2);
            }
        });

        // lambda写法
        Arrays.sort(arr, (s1, s2) -> {
            return s1.compareTo(s2);
        });

        // 直接引用已有的方法作为lambda函数（引用静态方法）
        // 方法签名一致即可。方法签名只看参数类型和返回类型，不看方法名称，也不看类的继承关系。
        Arrays.sort(arr, LearnLambda::cmp);

        // 引用实例方法
        // 实例方法的this也算一个参数
        Arrays.sort(arr, String::compareTo);

        // 引用构造方法，实现类似于python里的lamba批量包装
        List<String> names = List.of("Bob", "Alice", "Tim");
        List<Person> persons = names.stream().map(Person::new).collect(Collectors.toList());
        System.out.println(persons);

        // 总结：当函数需要的参数对应的接口有@FunctionalInterface时，就可以用同签名函数作为参数传递
        // 比如Arrays.sort的第二个参数和stream().map的参数
        // 该接口只有一个方法，与该方法的签名相同的函数即可

    }

    static int cmp(String s1, String s2) {
        return s1.compareTo(s2);
    }
}

class Person {
    String name;

    public Person(String name) {
        this.name = name;
    }

    public String toString() {
        return "Person: " + this.name;
    }
}