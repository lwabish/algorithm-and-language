import java.util.concurrent.locks.*;
import java.util.*;
class Counter{
    private final ReadWriteLock rwlock = new ReentrantReadWriteLock();
    private final Lock rlock = rwlock.readLock();
    private final Lock wlock = rwlock.writeLock();
    private int[] counts = new int[10];

    public void inc(int index){
        wlock.lock();
        try{
            counts[index] +=1;
        }finally{
            wlock.unlock();
        }
    }

    public int[] get(){
        rlock.lock();
        try{
            return Arrays.copyOf(counts, counts.length);
        }finally{
            rlock.unlock();
        }
    }
}