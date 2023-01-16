public class LearnThread2{
    public static void main(String[] args) throws Exception {
        Thread t = new Thread(
            ()->{
                System.out.println("thread done");
            }
        );
        System.out.println("start");
        t.start();
        // main线程调用t线程的join，main将等待t完成
        t.join();
        System.out.println("end");
    }
}