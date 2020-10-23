import java.io.InputStream;

public class LearnReadFromClassPath {
    public static void main(String[] args) throws Exception {
        InnerLearnReadFromClassPath i1 = new InnerLearnReadFromClassPath();

        try (InputStream input = i1.getClass().getResourceAsStream("/1.txt");) {
            if (input != null) {
                System.out.println(input.read());
            } else {
                System.out.println("未找到文件");
            }
        }

    }
}

/**
 * InnerLearnReadFromClassPath
 */
class InnerLearnReadFromClassPath {

    public InnerLearnReadFromClassPath() {

    }

}
