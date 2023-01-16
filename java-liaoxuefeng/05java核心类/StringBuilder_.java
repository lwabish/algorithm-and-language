public class StringBuilder_ {
    public static void main(String[] args) {
        // +字符串拼接内存效率低，StringBuilder比较高效
        // 编译器可以自动优化+，不需要手动使用StringBuilder
        // StringBuffer线程安全
        StringBuilder sb = new StringBuilder(1024);
        for (int i = 0; i < 1000; i++) {
            sb.append(",");
            // 支持链式操作
            sb.append(i).append("_").insert(0, "_");
        }
        String s = sb.toString();
        System.out.println(s);

    }
}