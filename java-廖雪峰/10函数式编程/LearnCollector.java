import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class LearnCollector {
    public static void main(String[] args) {
        // stream to list
        Stream<String> s1 = Stream.of("a", "b", "c");
        List<String> l1 = s1.map(String::toUpperCase).collect(Collectors.toList());
        System.out.println(l1);

        // stream to array
        List<String> l2 = List.of("Apple", "Banana", "Orange");
        String[] arr = l2.stream().toArray(String[]::new);
        System.out.println(Arrays.toString(arr));

        // stream to map
        Stream<String> s2 = Stream.of("APPL:apple", "MSFT:microsoft");
        Map<String, String> map = s2
                .collect(Collectors.toMap(s -> s.substring(0, s.indexOf(":")), s -> s.substring(s.indexOf(":") + 1)));
        System.out.println(map);

        // stream分组
        List<String> list = List.of("Apple", "Banana", "Blackberry", "Coconut", "Avocado", "Cherry", "Apricots");
        Map<String, List<String>> groups = list.stream()
                // 第一个参数：分组依据
                // 第二个参数：分组结果
                .collect(Collectors.groupingBy(s -> s.substring(0, 1), Collectors.toList()));
        System.out.println(groups);
    }
}
