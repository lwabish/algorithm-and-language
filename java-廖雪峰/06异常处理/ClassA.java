import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.Arrays;

public class ClassA {
    public static void main(String[] args) throws Exception {
        byte[] bs = toGBK("中文");
        System.out.println(Arrays.toString(bs));
        if (args.length > 0) {
            // 手抛异常
            throw new Exception();
        }
    }

    // 纯语法，不能跑
    private static byte[] toGBK(String s) {
        try {
            return s.getBytes("GBK");
        } catch (UnsupportedEncodingException e) {
            // 打印调用栈
            e.printStackTrace();
            return s.getBytes();
            // 多catch，注意顺序，子类在前，父类在后兜底
        } catch (IOException e) {
            System.out.println("e");
            return s.getBytes();
            // 可以多个一起写
        } catch (MBeanException | NumberFormatException e) {
            System.out.println(e);
            // 异常嵌套，避免丢失
            throw new Exception(NumberFormatException);
            return s.getBytes();
        } catch (Exception e) {
            // 暂存
            origin = e;
            return s.getBytes();
        } finally {
            System.out.println("done");
            Exception e = new IllegalAccessException();
            if (origin != null) {
                e.addSuppressed(origin);
            }
        }
    }
}
