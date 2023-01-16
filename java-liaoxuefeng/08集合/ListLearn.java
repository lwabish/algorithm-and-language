import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Objects;

public class ListLearn {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("apple");
        list.add("banana");
        list.add("pear");
        list.add("apple");
        // 允许加null
        list.add(null);
        System.out.println(list.size());
        System.out.println(list.get(4));

        // of 不能加null
        // list1是只读的
        List<Integer> list1 = List.of(1, 2, 3);
        System.out.println(list1);

        // 遍历List，不推荐的基本方法
        for (int i = 0; i < list.size(); i++) {
            System.out.println(list.get(i));
        }

        // 使用iterator屏蔽遍历细节
        for (Iterator<String> it = list.iterator(); it.hasNext();) {
            System.out.println(it.next());
        }

        // 简化上述语法
        for (String fruit : list) {
            System.out.println(fruit);
        }
        learnEquals();
    }

    private static void learnEquals() {
        List<Person> list2 = List.of(new Person("bob"), new Person("amy"));
        System.out.println(list2.contains(new Person("bob")));
    }
}

class Person {
    String name;

    Person(String name) {
        this.name = name;
    }

    // 覆写了equals方法，才可以实现在list里对比
    public boolean equals(Object o) {
        if (o instanceof Person) {
            Person p = (Person) o;
            return Objects.equals(this.name, p.name);
        }
        return false;
    }
}