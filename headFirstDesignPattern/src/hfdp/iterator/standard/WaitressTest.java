package hfdp.iterator.standard;

import java.util.ArrayList;

/**
 * @author Lwabish
 */
public class WaitressTest {
    public static void main(String[] args) {
        CakeMenu cakeMenu = new CakeMenu();
        DinerMenu dinerMenu = new DinerMenu();
        CafeMenu cafeMenu = new CafeMenu();

        Waitress waitress = new Waitress(new ArrayList<Menu>() {{
            add(cafeMenu);
            add(dinerMenu);
            add(cakeMenu);
        }});
        waitress.printMenu();
    }
}
