public class LearnThread7{
    public static void main(String[] args)throws Exception{
        Thread adder = new AddThread();
        Thread decer = new DecThread();

        adder.start();
        decer.start();

        adder.join();
        decer.join();

        System.out.println(Counter.count);
    }
}

class Counter{
    // 线程共享锁
    // 锁的设计：每个临界区一把锁，锁多了线程同步无效，锁少了影响效率。
    public static final Object lock = new Object();
    public static int count = 0;
}

class AddThread extends Thread{
    public void run(){
        for(int i=0;i<1000;i++){
            synchronized(Counter.lock){
                Counter.count+=1;
            }
        }
    }
}

class DecThread extends Thread{
    public void run(){
        for(int i=0;i<1000;i++){
            synchronized(Counter.lock){
                Counter.count-=1;
            }
        }
    }
}