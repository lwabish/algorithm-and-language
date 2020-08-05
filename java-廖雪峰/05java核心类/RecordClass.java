public class RecordClass {
    public static void main(String[] args) {
        Point p = new Point(215, 1);
        System.out.println(p.x());

        Point p1 = new Point(-1, -1);
        System.out.println(p1.x());
    }
}

// 不可变对象，自动生成基础方法
record Point(int x, int y) {
    // 为构造函数补充逻辑
    public Point {
        if (x < 0 || y < 0) {
            throw new IllegalArgumentException();
        }
    }

    // 可以设置静态方法，用于生成新的实例
    public static Point of(int x, int y) {
        return new Point(x, y);
    }
}