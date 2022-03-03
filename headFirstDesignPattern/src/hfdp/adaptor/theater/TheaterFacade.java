package hfdp.adaptor.theater;

/**
 * @author Lwabish
 */
public class TheaterFacade {

    Amplifier amplifier;

    Projector projector;

    public TheaterFacade(Amplifier a, Projector p) {
        this.amplifier = a;
        this.projector = p;
    }

    /**
     * 门面模式：
     * 将复杂的低层知识包装成简单的操作方式
     */
    public void watchMovie() {
        amplifier.on();
        projector.on();
    }
}
