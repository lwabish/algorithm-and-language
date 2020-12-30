public class LearnThread5{
    public static void main(String[] args)throws InterruptedException{
        Thread t = new Thread(
            ()-> {
                while(true){
                    try{
                        Thread.sleep(12);
                        System.out.println("thread");
                    }catch(InterruptedException e){
                        break;
                    }
                    
                }
            }
        );
        // 标记为守护线程
        // 非守护线程结束后，守护线程会随jvm一起结束，不需要维护
        t.setDaemon(true);
        t.start();
        // t.join();
        System.out.println("bye");
    }
}