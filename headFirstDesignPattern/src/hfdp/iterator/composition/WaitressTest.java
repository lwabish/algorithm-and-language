package hfdp.iterator.composition;

/**
 * @author Lwabish
 */
public class WaitressTest {
    public static void main(String[] args) {
        // 先构建三个菜单
        MenuComponent menu1 = new Menu("menu1", "menu1");
        MenuComponent menu2 = new Menu("menu2", "menu2");
        MenuComponent menu3 = new Menu("menu3", "menu3");

        // 再构建一个父菜单做根节点
        MenuComponent parent = new Menu("parent", "parent");
        parent.add(menu1);
        parent.add(menu2);


        // 给菜单增加菜单项
        menu1.add(new MenuItem("m1i1", "m1i1", false, 2.1));
        menu2.add(new MenuItem("m1i1", "m1i1", false, 2.1));
        menu3.add(new MenuItem("m1i1", "m1i1", false, 2.1));

        // 把menu3作为子菜单加入menu2
        menu2.add(menu3);

        Waitress waitress = new Waitress(parent);
        waitress.printMenu();
    }
}
