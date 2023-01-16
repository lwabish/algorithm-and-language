import java.util.*;
import java.util.concurrent.locks.*;
class TaskQueue{
    private final Lock lock = new ReentrantLock();
    private final Condition condition= lock.newCondition();
    private Queue<String> queue = new LinkedList<>();

    public void addTask(String s){
        lock.lock();
        try{
            queue.add(s);
            condition.signalAll();
        }finally{
            lock.unlock();
        }
    }

    public String getTask() throws Exception{
        lock.lock();
        try{
            while(queue.isEmpty()){
                condition.await();
            }
            return queue.remove();
        }finally{
            lock.unlock();
        }
    }
}