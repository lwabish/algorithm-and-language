public class LearnThread9 {
    public static void main(String[] args) throws Exception{
        CounterDead cd = new CounterDead();
        Thread t1 = new Thread(()->{
            cd.add(1);        
        });
        Thread t2 = new Thread(()->{
            cd.dec(1);
        });
        t1.start();
        t2.start();
        t1.join();
        t2.join();

        System.out.println(cd.count1);
        System.out.println(cd.count2);
    }
}

class CounterDead{
    public int count1;
    private static final Object lock1 = new Object();
    public int count2;
    private static final Object lock2 = new Object();

    public void add(int n){
        synchronized(this.lock1){
            System.out.println("count1 +");
            count1+=n;
            synchronized(this.lock2){
                System.out.println("count2 +");
                count2+=n;
            }
        }
    }

    public void dec(int n){
        synchronized(this.lock2){
            System.out.println("count2 -");
            count2-=n;
            synchronized(this.lock1){
                System.out.println("count2 +");
                count1-=n;
            }
        }
    }
}
class Counter{
    private int count=0;

    public synchronized void add(int n){
        if(n<0){
            // java锁的特性:可重入，拿到锁后可以再次调用需要加锁的方法，拿一样的锁。使用锁计数确保锁最终的正确释放。
            dec(-n);
        }else{
            count+=n;
        }
    }

    public synchronized void dec(int n){
        count-=n;
    }
}         