package hfdp.adaptor.theater;

/**
 * @author Lwabish
 */
public class WatchMovie {
    public static void main(String[] args) {
        TheaterFacade theaterFacade = new TheaterFacade(new Amplifier(), new Projector());
        theaterFacade.watchMovie();
    }
}
