import java.io.File;
import java.io.FilenameFilter;

public class LearnFile {
    public static void main(String[] args) {
        File f = new File("/Users/wubowen/Desktop/tmp");
        File[] fs1 = f.listFiles();
        printFiles(fs1);

        File[] fs2 = f.listFiles(new FilenameFilter() {
            public boolean accept(File dir, String name) {
                return name.endsWith("yml");
            }
        });
        printFiles(fs2);

    }

    static void printFiles(File[] files) {
        System.out.println("==========");
        if (files != null) {
            for (File file : files) {
                System.out.println(file);
            }
        }
        System.out.println("==========");
    }
}
