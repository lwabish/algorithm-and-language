import java.nio.file.Files;
import java.nio.file.Paths;
import java.time.DayOfWeek;
import java.time.LocalDate;
import java.util.Arrays;
import java.util.List;
import java.util.function.Supplier;
import java.util.stream.IntStream;
import java.util.stream.LongStream;
import java.util.stream.Stream;

public class LearnStream {
    public static void main(String[] args) throws Exception {
        createStream();
        mapExample();
        filterExample();
        reduceExample();
    }

    static void reduceExample() {
        // acc: reduce的累计值对象
        // n：stream元素
        int sum = Stream.of(1, 2, 3, 4, 5).reduce(0, (acc, n) -> acc + n);
        System.out.println(sum);
    }

    static void filterExample() {
        List.of(1, 2, 3, 4).stream().filter(x -> x % 2 == 0).forEach(System.out::println);

        Stream.generate(new LocalDateSupplier()).limit(31)
                .filter(ldt -> ldt.getDayOfWeek() == DayOfWeek.SATURDAY || ldt.getDayOfWeek() == DayOfWeek.SUNDAY)
                .forEach(System.out::println);
    }

    static void mapExample() {
        List.of("a", "b", "c").stream().map(String::toUpperCase).forEach(System.out::println);

    }

    static void createStream() {
        Stream<String> s1 = Stream.of("a", "b", "c");
        s1.forEach(System.out::println);

        Stream<String> s2 = Arrays.stream(new String[] { "1", "2", "3" });
        s2.forEach(System.out::println);

        Stream<String> s3 = List.of("x", "y", "z").stream();
        s3.forEach(System.out::println);

        Stream<Integer> s4 = Stream.generate(new NatualSupplier());
        s4.limit(10).forEach(System.out::println);

        // 把文本文件按行变成stream
        try (Stream<String> lines = Files.lines(Paths.get("1.txt"))) {
            lines.forEach(System.out::println);
        } catch (Exception e) {
            e.printStackTrace();
        }

        // 其他： Pattern.compile("\\s+").splitAsStream()

        // 基于基本类型的stream，可提高效率
        IntStream is = Arrays.stream(new int[] { 1, 2, 3 });
        LongStream ls = List.of("1", "2", "3").stream().mapToLong(Long::parseLong);
        is.forEach(System.out::println);
        ls.forEach(System.out::println);
    }
}

// 自然数序列生成
class NatualSupplier implements Supplier<Integer> {
    int n = 0;

    public Integer get() {
        n++;
        return n;
    }
}

// 日期生成
class LocalDateSupplier implements Supplier<LocalDate> {
    LocalDate start = LocalDate.of(2020, 1, 1);
    int n = -1;

    public LocalDate get() {
        n++;
        return start.plusDays(n);
    }
}