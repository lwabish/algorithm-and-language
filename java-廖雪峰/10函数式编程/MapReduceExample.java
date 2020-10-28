import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MapReduceExample {
    public static void main(String[] args) {
        List<String> props = List.of("profile=native", "debug=true", "logging=warn", "interval=500");
        Map<String, String> map = props.stream().map(kv -> {
            String[] ss = kv.split("\\=", 2);
            return Map.of(ss[0], ss[1]);
        }).reduce(new HashMap<String, String>(), (m, kv) -> {
            m.putAll(kv);
            return m;
        });

        map.forEach((k, v) -> {
            System.out.println(k + " = " + v);
        });
    }
}
