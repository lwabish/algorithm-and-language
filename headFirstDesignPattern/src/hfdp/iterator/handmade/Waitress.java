package hfdp.iterator.handmade;

/**
 * @author Lwabish
 */
public class Waitress {
    CakeMenu cakeMenu;
    DinerMenu dinerMenu;

    public Waitress(CakeMenu cakeMenu, DinerMenu dinerMenu) {
        this.cakeMenu = cakeMenu;
        this.dinerMenu = dinerMenu;
    }

    public void printMenu() {
        // 省略了外部Iterator，直接把iterator写在了Menu类里
        printMenu(cakeMenu);
        printMenu(dinerMenu);
    }

    private void printMenu(Iterator iterator) {
        while (iterator.hasNext()) {
            MenuItem menuItem = (MenuItem) iterator.next();
            System.out.println(menuItem.getName());
        }
    }
}
