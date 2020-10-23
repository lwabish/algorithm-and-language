import java.io.ByteArrayOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;

public class LearnOutputStream {
    public static void main(String[] args) throws Exception {

        test1();
        test2();
        test3();

    }

    static void test1() throws IOException {
        OutputStream o1 = new FileOutputStream(
                "/Users/wubowen/cloud/Projects/0_algorithm_language/java-廖雪峰/09IO/2.txt");
        // H
        o1.write(72);
        // e
        o1.write(101);
        o1.close();
    }

    static void test2() throws IOException {
        try (OutputStream o2 = new FileOutputStream(
                "/Users/wubowen/cloud/Projects/0_algorithm_language/java-廖雪峰/09IO/2.txt")) {
            o2.write("Hello".getBytes());
        }
    }

    static void test3() throws IOException {
        byte[] data;
        try (ByteArrayOutputStream o3 = new ByteArrayOutputStream()) {
            o3.write("hello".getBytes());
            data = o3.toByteArray();
        }
        System.out.println(new String(data));
    }
}
