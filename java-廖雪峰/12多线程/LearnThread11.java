import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.locks.Lock;
public class LearnThread11{
    public static void main(String[] args){
        Counter c = new Counter();
        Thread t1 = new Thread(            
            ()->{
                System.out.println("add");
                c.add(10);
            }
            );
        t1.start();
        
    }
}

class Counter{
    private final Lock lock = new ReentrantLock();
    private int count;
    public void add(int n){
        lock.lock();
        try{
            count +=n;
        // 必须手工释放锁
        }finally{
            lock.unlock();
        }

    }
}