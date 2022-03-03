package hfdp.template.ducksort;

import java.util.Arrays;

/**
 * @author Lwabish
 */
public class SortDucks {
    public static void main(String[] args) {
        Duck[] ducks = {
                new Duck("d1", 1),
                new Duck("d1", 3),
                new Duck("d1", 2),
        };
        Arrays.sort(ducks);

        for (Duck duck : ducks) {
            System.out.println(duck);
        }
    }
}
