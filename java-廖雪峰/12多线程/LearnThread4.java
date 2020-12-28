public class LearnThread4{
    public static void main(String[] args)throws InterruptedException{
        Thread t = new Mythread();
        t.start();
        Thread.sleep(1000);
        // 发送中断请求
        t.interrupt();
        t.join();
        System.out.println("end");
    }
}

class Mythread extends Thread{
    public void run(){
        HelloThread hello = new HelloThread();
        hello.start();
        try{
            hello.join();
        // 捕获异常，获取被中断的信号
        }catch(InterruptedException e){
            System.out.println("interrupted");
            hello.interrupt();
            // 方法2
            hello.running=false;
        }
    }
}

class HelloThread extends Thread{
    // 方法2：用running属性判断是否被终止
    // volatile: jvm立即同步属性的值，避免多线程使用属性时拿到的值不是最新的
    public volatile boolean running = true;
    public void run(){
        int n=0;
        while(running || ! interrupted() ){
            n++;
            System.out.println(n+" hello!");
            try{
                Thread.sleep(100);
            }catch(InterruptedException e){
                break;
            }
        }
    }
}
