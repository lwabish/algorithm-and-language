import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.InputStream;

public class LearnFilter {
    public static void main(String[] args) throws Exception {
        // 数据源类的InputStream
        InputStream f = new FileInputStream("/Users/wubowen/cloud/Projects/0_algorithm_language/java-liaoxuefeng/09IO/1.txt");

        // 辅助功能类的InputStream对数据源类进行一次包装
        // 此处和python中的装饰器原理类似
        InputStream f_buffered = new BufferedInputStream(f);

        try {
            System.out.println(f_buffered.read());
        } catch (Exception e) {
            System.out.println(e);
        } finally {
            f_buffered.close();
        }
    }
}
