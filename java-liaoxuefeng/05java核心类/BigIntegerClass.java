import java.math.BigInteger;

public class BigIntegerClass {
    public static void main(String[] args) {
        BigInteger b1 = new BigInteger("1111111111111");
        BigInteger b2 = new BigInteger("12345555");
        BigInteger b3 = b1.add(b2);
        System.out.println(b3);

        System.out.println(b3.floatValue());

    }
}