import java.io.ByteArrayInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

public class LearnInputStream {
    public static void main(String[] args) throws Exception {
        readFile();
        readWithBuffer();
        simulateInputStream();
        testReadAsString();
    }

    // 所有与IO操作相关的代码都必须正确处理IOException
    public static void readFile() throws IOException {
        // try参数中的资源如果实现了AutoCloseable接口，则编译器自动关闭
        try (InputStream input = new FileInputStream(
                "/Users/wubowen/cloud/Projects/0_algorithm_language/java-廖雪峰/09IO/1.txt")) {
            int n;
            while ((n = input.read()) != -1) {
                System.out.println(n);
            }
        }
    }

    public static void readWithBuffer() throws IOException {
        try (InputStream input = new FileInputStream(
                "/Users/wubowen/cloud/Projects/0_algorithm_language/java-廖雪峰/09IO/1.txt")) {
            byte[] buffer = new byte[3];
            int n;
            for (;;) {
                n = input.read(buffer);
                if (n == -1) {
                    break;
                }
                System.out.println("read " + n + " bytes.");
            }
        }
    }

    // 手工构造字节数组代替文件，供inputStream读
    public static void simulateInputStream() throws IOException {
        byte[] data = { 97, 98, 99 };
        try (InputStream input = new ByteArrayInputStream(data)) {
            int n;
            while ((n = input.read()) != -1) {
                System.out.println((char) n);
            }
        }
    }

    // 面向抽象编程,接收一个InputStream，但是实际传进来的可以是InputStream的各个子类实现
    public static String readAsString(InputStream input) throws IOException {
        int n;
        StringBuilder sb = new StringBuilder();
        while ((n = input.read()) != -1) {
            sb.append(n);
        }
        return sb.toString();
    }

    public static void testReadAsString() throws IOException {
        // readAsString函数既可以接收FileInputStream
        try (InputStream i1 = new FileInputStream(
                "/Users/wubowen/cloud/Projects/0_algorithm_language/java-廖雪峰/09IO/1.txt")) {
            System.out.println(readAsString(i1));
        }

        // 又可以接收ByteInputStream
        try (InputStream i2 = new ByteArrayInputStream(new byte[] { 1, 2, 3, 4 })) {
            System.out.println(readAsString(i2));
        }
    }

}
