import java.math.BigDecimal;
import java.math.RoundingMode;

public class BigDecimalClass {
    public static void main(String[] args) {
        BigDecimal bd = new BigDecimal("123.455");
        BigDecimal bd1 = bd.multiply(bd);
        System.out.println(bd1);

        // 取小数位数
        System.out.println(bd.scale());
        System.out.println(bd1.scale());

        // 截断
        BigDecimal bd3 = bd1.setScale(2, RoundingMode.HALF_UP);
        System.out.println(bd3);

        // 除法
        BigDecimal bd4 = bd1.divide(bd, 3, RoundingMode.HALF_UP);
        System.out.println(bd4);

        // 除法求余
        BigDecimal[] bd2 = bd1.divideAndRemainder(bd);
        System.out.println(bd2[0]);
        System.out.println(bd2[1]);
        // 正负or0
        System.out.println(bd2[1].signum());

        // 比较
        // 相等-0 小于-负数 大于-正数
        System.out.println(bd1.compareTo(bd));
    }
}