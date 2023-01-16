public class LearnThread8{
    public static void main(String[] args)throws Exception{
        //线程对临界区不需要考虑加锁，直接用即可，即该临界类是线程安全的
        Counter c1 =new Counter();

        Thread t1 =new Thread(
            ()->{
                c1.add(1);
            }
        );
        Thread t2 = new Thread(
            ()->{
                c1.dec(1);
            }
        );
        t1.start();
        t2.start();

        t1.join();
        t2.join();

        System.out.println(c1.getCount());

    }
}

/**
 *哪些类是线程安全的
 * 1. 经过设计的自定义类，使用synchronized确保了临界区原子性
 * 2. java.lang.StringBuffer
 * 3. 不变类：String Integer LocalDate等，因为成员变量都是final修饰的，多线程访问只能读不能写
 * 4. Math等类，只有静态方法，没有成员变量
 * 5. 非线程安全的类，但是多线程对临界区不写只读，也是线程安全的
 */

//一个线程安全的类
class Counter{
    private int count = 0;
    public int getCount(){
        return count;
    }

    public void add(int n){
        // 锁住实例
        synchronized(this){
            count+=n;
        }
    }

    // 和add方法效果一致，语法不一样
    public synchronized void dec(int n){
        count -=n;
    }

    //对静态方法加锁，相当于锁住该类由jvm管理的Class类的实例
    public synchronized static void test(){

    }

    //上面的等价于
    public static void test1(){
        synchronized(Counter.class){
            
        }
    }
}

