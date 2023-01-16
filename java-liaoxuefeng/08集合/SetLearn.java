import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;

public class SetLearn {
    public static void main(String[] args) {
        // hashset无序
        Set<String> set = new HashSet<>();
        System.out.println(set.add("a"));
        System.out.println(set.contains("a"));
        System.out.println(set.remove("a"));
        System.out.println(set.size());

        // treeset 按comparable的顺序排序
        Set<String> set1 = new TreeSet<>();
        set1.add("a");
        set1.add("b");
        set1.add("c");

        for (String s : set1) {
            System.out.println(s);
        }
    }
}
