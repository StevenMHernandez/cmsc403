import java.util.*;
import java.util.concurrent.locks.*;
import java.util.concurrent.TimeUnit;

class Giver {
    public void run(FoodBank foodBank) {
        Integer randomInt = (new Random()).nextInt(10);
        foodBank.giveFood(randomInt);
    }
}

class Taker {
    public void run(FoodBank foodBank) {
        Integer randomInt = (new Random()).nextInt(100);
        foodBank.takeFood(randomInt);
    }
}

class FoodBank {
    public Lock lock;
    public Condition canRemove;
    public Integer foodRemaining = 0;

    public FoodBank() {
        lock = new ReentrantLock();
        canRemove = lock.newCondition();
    }

    public void giveFood(Integer count) {
        lock.lock();
        try {
            System.out.println(String.format("(%d items) Giver: Adding %d items of food . . .", foodRemaining, count));
            foodRemaining += count;
            System.out.println(String.format("(%d items) Giver: Added %d items of food\n", foodRemaining, count));
            canRemove.signal();
        } finally {
            lock.unlock();
        }
    }

    public void takeFood(Integer count) {
        lock.lock();
        try {
            while (foodRemaining < count) {
                System.out.println(String.format("(%d items) Taker: Waiting for  %d items of food", foodRemaining, count));
                canRemove.await();
            }
            System.out.println(String.format("(%d items) Taker: Removing %d items of food . . .", foodRemaining, count));
            foodRemaining -= count;
            System.out.println(String.format("(%d items) Taker: Removed %d items of food\n", foodRemaining, count));
        } catch (InterruptedException exception) {
            // pass
        } finally {
            lock.unlock();
        }
    }
}

class Main {
    public static void main(String[] arg) {
        FoodBank foodBank = new FoodBank();
        Giver giver = new Giver();
        Taker taker = new Taker();

        (new Thread(() -> { while (true) { giver.run(foodBank); } })).start();
        (new Thread(() -> { while (true) { taker.run(foodBank); } })).start();
    }
}