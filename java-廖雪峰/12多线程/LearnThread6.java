// 示例：临界区不加锁
public class LearnThread6 {
    public static void main(String[] args)throws Exception{
        Thread adder = new AddThread();
        Thread decer = new DecThread();

        adder.start();
        decer.start();

        // 阻塞，确保加减执行完再打印
        adder.join();
        decer.join();

        System.out.println(Counter.count);
    }
}

class Counter{
    public static int count = 0;
}

class AddThread extends Thread{
    public void run(){
        // 是否需要线程同步，关键看线程执行的操作是否
        for(int i=0;i<10000;i++){Counter.count+=1;}
    }
}

class DecThread extends Thread{
    public void run(){
        for(int i=0;i<10000;i++){Counter.count -=1;}
    }
}