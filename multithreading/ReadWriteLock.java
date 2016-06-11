/* Implementation of read and write locks and an example illustrating read and write concurrency. */
class ReadWriteLock {
    private boolean readFree = true;
    private boolean writeFree = true;
    private int readCount = 0;

    public void acquireRead() {
        if (!getReadFree()) {
            while(true) {
                if (getReadFree())
                    break;
            }
        }

        setWriteFree(false);
        incReadCount();
    }

    public void releaseRead() {
        if (getNumReaders() <= 0) {
            clearReadCount();
            setWriteFree(true);
            return;
        }

        decReadCount();

        if (getNumReaders() <= 0)
            setWriteFree(true);
    }

    public void acquireWrite() {
        if (!getWriteFree()) {
            while(true) {
                if (getWriteFree())
                    break;
            }
        }

        setWriteFree(false);
        setReadFree(false);
    }

    public void releaseWrite() {
        setWriteFree(true);
        setReadFree(true);
    }

    public synchronized int getNumReaders() {
        return readCount;
    }

    private synchronized void decReadCount() {
        readCount--;
    }

    private synchronized void clearReadCount() {
        readCount = 0;
    }

    private synchronized void incReadCount() {
        readCount++;
    }

    private synchronized void setReadFree(boolean b) {
        readFree = b;
    }

    private synchronized void setWriteFree(boolean b) {
        writeFree = b;
    }

    private synchronized boolean getReadFree() {
        return readFree;
    }

    private synchronized boolean getWriteFree() {
        return writeFree;
    }

    public static void main(String[] args) {
        int[] arr = new int[]{0, 1, 2, 3, 4, 5, 6};
        ReadWriteLock lock = new ReadWriteLock();

        Read r0 = new Read(0, arr, 0, lock);
        Read r1 = new Read(1, arr, 0, lock);
        Read r2 = new Read(2, arr, 0, lock);
        Read r3 = new Read(3, arr, 0, lock);
        Read r4 = new Read(4, arr, 0, lock);
        Read r5 = new Read(5, arr, 0, lock);
        Read r6 = new Read(6, arr, 0, lock);
        Write w1 = new Write(1, arr, 0, -1, lock);
        Write w2 = new Write(2, arr, 0, -2, lock);
        Write w3 = new Write(3, arr, 0, -3, lock);
        Write w4 = new Write(4, arr, 0, -4, lock);

        System.out.println("-----------");
        new Thread(w1).start();
        new Thread(w2).start();
        new Thread(w3).start();
        new Thread(r0).start();
        new Thread(r1).start();
        new Thread(r2).start();
        new Thread(r3).start();
        new Thread(w4).start();
        new Thread(r4).start();
        new Thread(r5).start();
        new Thread(r6).start();
        

    }
}

class Read implements Runnable {
    private int[] arr;
    private int pos;
    private int id;
    private int count = 0;
    private ReadWriteLock lock;

    public Read(int id, int[] arr, int pos, ReadWriteLock lock) {
        this.id = id;
        this.arr = arr;
        this.pos = pos;
        this.lock = lock;
    }

    @Override
    public void run() {
        System.out.printf("Starting thread R%d.\n", id);

        try {
            lock.acquireRead();
            while (count < 5) {
                System.out.printf("In Thread R%d, itr: %d.numReaders:%d\n", id, count, lock.getNumReaders());
                Thread.sleep(500);
                count++;
            }
        } catch(InterruptedException e) {
            System.out.printf("Exception in Thread R%d.\n", id);
        } finally {
            lock.releaseRead();
            System.out.printf("Completeted thread R%d, read value:%d, pos:%d. numReaders:%d\n", id, arr[pos], pos, lock.getNumReaders());
        }
    }

}
 

class Write implements Runnable {
    private int[] arr;
    private int pos;
    private int value;
    private int id;
    private int count = 0;
    private ReadWriteLock lock;

    public Write(int id, int[] arr, int pos, int value, ReadWriteLock lock) {
        this.id = id;
        this.arr = arr;
        this.pos = pos;
        this.value = value;
        this.lock = lock;
    }

    @Override
    public void run() {
        System.out.println("Starting thread W" + id);

        try {
            lock.acquireWrite();
            while (count < 5) {
                System.out.printf("In Thread W%d, current count is: %d.\n", id, count);
                Thread.sleep(500);
                count++;
            }
        } catch(InterruptedException e) {
            System.out.printf("Exception in Thread W%d.\n", id);
        } finally {
            arr[pos] = value;
            lock.releaseWrite();

        }
       System.out.println("Completed thread W" + id);
    }

}



