import java.io.CharArrayReader;
import java.io.FileReader;
import java.io.Reader;
import java.io.StringReader;
import java.nio.charset.StandardCharsets;
import java.io.InputStreamReader;
import java.io.FileInputStream;

public class LearnReader {
    public static void main(String[] args) throws Exception {
        try (Reader reader = new FileReader("/Users/wubowen/cloud/Projects/0_algorithm_language/java-廖雪峰/09IO/1.txt",
                StandardCharsets.UTF_8);) {
            for (;;) {
                int n = reader.read();
                if (n == -1) {
                    break;
                }
                System.out.println((char) n);
            }
        }

        try (Reader reader1 = new FileReader("/Users/wubowen/cloud/Projects/0_algorithm_language/java-廖雪峰/09IO/1.txt",
                StandardCharsets.UTF_8)) {
            char[] buffer = new char[1000];
            int n;
            while ((n = reader1.read(buffer)) != -1) {
                System.out.println("read " + n + " chars");
            }
        }

        // 从其他来源read的Reader
        try (Reader reader = new CharArrayReader("Hello".toCharArray())) {
        }
        try (Reader reader = new StringReader("Hello")) {
        }
        // 将InputStream转为reader
        try (Reader reader = new InputStreamReader(
                new FileInputStream("/Users/wubowen/cloud/Projects/0_algorithm_language/java-廖雪峰/09IO/1.txt"),
                "UTF-8")) {
            // TODO:
        }

    }
}
