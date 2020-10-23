import java.io.FileInputStream;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

public class LearnZip {
    public static void main(String[] args) throws Exception {

        // read zip
        try (ZipInputStream zip = new ZipInputStream(
                new FileInputStream("/Users/wubowen/cloud/Projects/0_algorithm_language/java-廖雪峰/09IO/1.zip"))) {
            ZipEntry entry;
            while ((entry = zip.getNextEntry()) != null) {
                String name = entry.getName();
                if (!entry.isDirectory()) {
                    System.out.println(name);
                    // 开始读字节，略
                }
            }
        }

        // write zip
        // 略，用到再说
    }
}
