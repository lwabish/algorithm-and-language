package hfdp.decorator;

import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

/**
 * @author wubowen
 */
public class LowerCaseTest {
    public static void main(String[] args) {
        int c;
        try {
            // idea里需要写绝对路径才能找到文件
            InputStream in = new LowerCaseInputStream(new BufferedInputStream(new FileInputStream("lowercase.txt")));
            while ((c = in.read()) >= 0) {
                System.out.print((char) c);
            }
            in.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
