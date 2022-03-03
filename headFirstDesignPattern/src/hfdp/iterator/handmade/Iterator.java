package hfdp.iterator.handmade;

/**
 * @author Lwabish
 */
public interface Iterator {
    /**
     * 是否还有元素可以迭代
     *
     * @return boolean
     */
    boolean hasNext();

    /**
     * 获取下一个元素
     *
     * @return 元素
     */
    Object next();
}
