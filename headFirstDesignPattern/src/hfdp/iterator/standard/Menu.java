package hfdp.iterator.standard;

import hfdp.iterator.handmade.MenuItem;

import java.util.Iterator;

/**
 * @author Lwabish
 */
public interface Menu {
    /**
     * 返回一个迭代器
     *
     * @return 迭代器
     */
    Iterator<MenuItem> createIterator();
}
