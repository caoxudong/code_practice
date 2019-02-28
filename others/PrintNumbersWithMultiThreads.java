package com.example.demo.puzzles;

import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingDeque;
import java.util.concurrent.ThreadFactory;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * 
 * <p>
 * 问题： 假设有n个线程，如何令这个n的线程轮流打印递增序列？
 * 
 * <p>
 * 例如：有3个线程，打印如下：
 * <ul>
 * <li>线程1： 1</li>
 * <li>线程2： 2</li>
 * <li>线程3： 3</li>
 * <li>线程1： 4</li>
 * <li>线程2： 5</li>
 * <li>线程3： 6</li>
 * <li>线程1： 7</li>
 * <li>线程2： 8</li>
 * <li>...</li>
 * </ul>
 * 
 * @author caoxudong
 *
 */
public class PrintNumbersWithMultiThreads {

    private static LinkedBlockingDeque bus = new LinkedBlockingDeque<Integer>(1);

    public static void main(String[] args) throws InterruptedException {
        System.out.println("test, maxNumber = " + 10 + ", threadsCount = 3");
        printNumber(10, 3);
    }

    private static void printNumber(int maxNumber, int threadsCount) throws InterruptedException {
        Thread[] threads = new Thread[threadsCount];
        Task[] tasks = new Task[threadsCount];
        InnerThreadsFactory innerThreadsFactory = new InnerThreadsFactory();
        for (int i = 0; i < threadsCount; i++) {
            Task task = new Task();
            tasks[i] = task;
            threads[i] = innerThreadsFactory.newThread(task);
            threads[i].start();
        }

        {
            int i = 0;
            do {
                Task task = tasks[(i + threadsCount) % threadsCount];
                task.pushNumber(i + 1);
                i++;
                bus.take();
            } while (i < maxNumber);
        }
        for (int i = 0; i < threadsCount; i++) {
            Task task = tasks[i];
            task.pushNumber(-1);
        }
    }

    private static class InnerThreadsFactory implements ThreadFactory {

        private AtomicInteger counter = new AtomicInteger(0);

        @Override
        public Thread newThread(Runnable r) {
            return new Thread(r, "thread-" + counter.addAndGet(1));
        }

    }

    private static class Task implements Runnable {
        private BlockingQueue<Integer> queue;

        public Task() {
            super();
            this.queue = new LinkedBlockingDeque<Integer>(1);
        }

        public void pushNumber(int value) throws InterruptedException {
            this.queue.put(value);
        }

        @Override
        public void run() {
            while (true) {
                Integer value;
                try {
                    value = queue.take();
                } catch (InterruptedException e) {
                    value = null;
                }
                if ((value == null) || (value.intValue() < 0)) {
                    return;
                }
                Thread currentThread = Thread.currentThread();
                System.out.println("print " + currentThread.getName() + "\t" + value);
                System.out.flush();
                try {
                    PrintNumbersWithMultiThreads.bus.put(0);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }

    }

}
