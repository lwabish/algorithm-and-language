package hfdp.iterator.standard;

/**
 * @author Lwabish
 */
public class WaitressTest {
    public static void main(String[] args) {
        CakeMenu cakeMenu = new CakeMenu();
        DinerMenu dinerMenu = new DinerMenu();
        CafeMenu cafeMenu = new CafeMenu();

        Waitress waitress = new Waitress(cakeMenu, dinerMenu, cafeMenu);
        waitress.printMenu();
    }
}
