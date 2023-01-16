public class LearnThread1{
    public static void main(String[] args)  {
        // do nothing
        Thread t = new Thread();
        // 虽然Thread类实现的是run方法，但是启动新线程必须通过start方法。看源码可知，start调用了一个用native修饰的方法，该方法由虚拟机执行，而不是由java本身执行。
        t.start();

        // 方法1
        Thread t1 = new MyThread();
        t1.start();

        // 方法2
        Thread t2 = new Thread(new MyRunnable());
        t2.start();

        // 方法2+lambda
        Thread t3 = new Thread(
            () -> {
                System.out.println("new thread 3");
            }
        );
        t3.setPriority(2);
        t3.start();

        // 验证主线程和其他线程的异步执行
        compareOrder();
    }

    static void compareOrder(){
        System.out.println("main start");
        Thread t = new Thread(){
            public void run(){
                System.out.println("thread start");
                try{
                    Thread.sleep(1000);
                }catch(Exception e){}
                
                System.out.println("thread end");
            }
        };
        t.start();
        try{
            Thread.sleep(20);
        }catch(Exception e){}
        System.out.println("main end");
    }
}

// 实现自己的线程类
// 方法1：
class MyThread extends Thread{
    @Override
    public void run(){
        System.out.println("new thread 1");
    }
}

// 方法2：
class MyRunnable implements Runnable{
    @Override
    public void run(){
        System.out.println("new thread 2");
    }
}

