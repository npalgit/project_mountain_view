/** A simple program that demonstrates concurrency. */
class SimpleMultiThread {
    public static void main(String[] args) {
        // Creatings threads
        SimpleThread t0 = new SimpleThread(0);
        SimpleThread t1 = new SimpleThread(1);
        SimpleThread t2 = new SimpleThread(2);
        SimpleThread t3 = new SimpleThread(3);
        SimpleThread t4 = new SimpleThread(4);

        new Thread(t0).start();
        new Thread(t1).start();
        new Thread(t2).start();
        new Thread(t3).start();
        
    }
}

class SimpleThread implements Runnable {
    private int id = 0;
    public int count = 0;
    public SimpleThread(int id) {
        this.id = id;
    }

    @Override
    public void run() {
        System.out.println("Starting thread #" + id);

        try {
            while (count < 5) {
                System.out.printf("In Thread #%d, current count is: %d.\n", id, count);
                Thread.sleep(500);
                count++;
            }
        } catch(InterruptedException e) {
            System.out.printf("Exception in Thread #%d.\n", id);
        }
        System.out.println("Completed thread #" + id);
    }
}
