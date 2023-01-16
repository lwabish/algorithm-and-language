import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class LearnFilesAndPaths {
    public static void main(String[] args) throws Exception {

        // 读
        byte[] data = Files.readAllBytes(Paths.get("1.txt"));

        String data1 = Files.readString(Paths.get("1.txt"));

        List<String> lines = Files.readAllLines(Paths.get("1.txt"));

        System.out.println(data);
        System.out.println(data1);
        System.out.println(lines);

        // 写
        byte[] data2 = new byte[] { 1, 2, 3 };
        Files.write(Paths.get("1"), data2);
        // 也可写入lines或text

    }
}
