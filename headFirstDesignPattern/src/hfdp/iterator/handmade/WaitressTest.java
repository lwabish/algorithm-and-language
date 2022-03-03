package hfdp.iterator.handmade;

/**
 * @author Lwabish
 */
public class WaitressTest {
    public static void main(String[] args) {
        CakeMenu cakeMenu = new CakeMenu();
        DinerMenu dinerMenu = new DinerMenu();

        Waitress waitress = new Waitress(cakeMenu, dinerMenu);
        waitress.printMenu();
    }
}
