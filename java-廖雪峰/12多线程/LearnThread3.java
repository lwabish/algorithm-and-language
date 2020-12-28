public class LearnThread3{
    public static void main(String[] args) throws InterruptedException {
        Thread t = new MyThread();
        t.start();
        Thread.sleep(1);
        // 发送中断线程请求
        t.interrupt();
        t.join();
        System.out.println("end");
    }
}

class MyThread extends Thread{
    public void run(){
        int n=0;
        // 检测是否收到了中断请求
        while(! isInterrupted()){
            n++;
            System.out.println(n+" hello");
        }
    }
}