import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.Arrays;
import java.util.Random;

public class OtherTools {
    public static void main(String[] args) {
        // math
        Math.abs(10);
        Math.max(1, 3);

        // random
        Random r = new Random();
        System.out.println(r.nextInt());
        System.out.println(r.nextInt(100));

        // secure random
        SecureRandom sr = null;
        try {
            sr = SecureRandom.getInstanceStrong();
        } catch (NoSuchAlgorithmException e) {
            sr = new SecureRandom();
        }
        byte[] buffer = new byte[16];
        sr.nextBytes(buffer);
        System.out.println(Arrays.toString(buffer));
    }
}