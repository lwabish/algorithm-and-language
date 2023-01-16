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

//java内的原子操作：
//单条 除double和long以外的基本类型赋值语句 和 引用类型赋值语句
//long 和 double在x64是原子的，但是没有明确规定

// 临界变量方法的局部变量是线程安全的
class Pair{
    int[] pair;
    public void set (int first, int last){
        //局部变量，线程安全
        int[] ps = new int[]{first, last};
        //单条引用赋值，线程安全，如果是多条语句，则要考虑加锁
        this.pair = ps;
    }
}