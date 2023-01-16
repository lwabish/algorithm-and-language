public class Wrapping {
    public static void main(String[] args) {
        int i = 100;
        // 使用静态工厂方法而不是new创建新的对象，给实现者优化的机会
        Integer i1 = Integer.valueOf(i);
        Integer i2 = Integer.valueOf("1");
        System.out.println(i1);
        System.out.println(i2.intValue());

        // auto boxing,但是影响编译效率
        Integer i3 = 100;
        int i4 = i3;
        System.out.println(i4);

        // 包装类不可变
        // Integer类的整型转换类方法
        System.out.println(Integer.toString(1024, 2));
        System.out.println(Integer.toHexString(178));

        // 包装类的预置常量
        System.out.println(Long.MAX_VALUE);

        // Number是所有包装类的父类
        Number num = Integer.valueOf(199);
        float f = num.floatValue();
        System.out.println(f);

        // 通过包装类转换出无符号数
        byte x = -1;
        byte y = 127;
        System.out.println(Byte.toUnsignedInt(x));
        System.out.println(Byte.toUnsignedInt(y));

    }
}