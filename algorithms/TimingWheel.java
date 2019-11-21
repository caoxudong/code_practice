package com.example.demo.structure;

import java.util.Random;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.atomic.AtomicInteger;

public class TimingWheel {

    private static final int TIMES = 60;

    private AtomicInteger l0 = new AtomicInteger(0);
    private AtomicInteger l1 = new AtomicInteger(0);
    private ArrayBlockingQueue<Task>[][] grids =
            new ArrayBlockingQueue[TIMES][];
    {
        for (int i = 0; i < TIMES; i++) {
            grids[i] = new ArrayBlockingQueue[TIMES];
            for (int j = 0; j < TIMES; j++) {
                grids[i][j] = new ArrayBlockingQueue<>(16);
            }
        }
    }

    private Thread timingThread = new Thread(() -> {
        while (true) {
            int l0Value = l0.get();
            int l1Value = l1.get();
            ArrayBlockingQueue<Task> tasksQueeu = grids[l0Value][l1Value];
            Task task;
            while ((task = tasksQueeu.poll()) != null) {
                task.execute();
            }
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            int newL0Value = l0.incrementAndGet();
            if (newL0Value >= TIMES) {
                l0.set(newL0Value % TIMES);
                int newL1Value = (l1Value + 1) % TIMES;
                l1.set(newL1Value);
            }
        }
    });

    public boolean addTask(Task task, int delayInSeconds) {
        int l0Value = delayInSeconds % TIMES;
        int l1Value = delayInSeconds / TIMES;
        boolean addResult = grids[l0Value][l1Value].add(task);
        return addResult;
    }

    public void start() {
        timingThread.start();
    }

    public static void main(String[] args) throws InterruptedException {
        TimingWheel timingWheel = new TimingWheel();
        Random random = new Random();
        int max = TIMES * TIMES;
        for (int i = 0; i < max; i++) {
            int delayInSeconds = random.nextInt(max);
            long nowInNano = System.nanoTime();
            TaskImpl taskImpl = new TaskImpl(nowInNano, 0L, delayInSeconds);
            timingWheel.addTask(taskImpl, delayInSeconds);
        }
        timingWheel.start();
        while (true) {
            Thread.sleep(10000);
        }
    }

    private static interface Task {
        void execute();
    }

    private static class TaskImpl implements Task {
        private long addTaskInNano;
        private long executeTaskInNano;
        private int execptedDelayInSeconds;

        public TaskImpl(long addTaskInNano, long executeTaskInNano,
                int execptedDelayInSeconds) {
            super();
            this.addTaskInNano = addTaskInNano;
            this.executeTaskInNano = executeTaskInNano;
            this.execptedDelayInSeconds = execptedDelayInSeconds;
            System.out.println("create teask, addTaskInNano=" + addTaskInNano
                + ", executeTaskInNano=" + executeTaskInNano
                + ", execptedDelayInSeconds=" + execptedDelayInSeconds);
        }

        @Override
        public void execute() {
            executeTaskInNano = System.nanoTime();
            long actualDelayInSeconds =
                    (executeTaskInNano - addTaskInNano) / 1000000;
            System.out.println("execute task, addTaskInNano=" + addTaskInNano
                + ", executeTaskInNano=" + executeTaskInNano
                + ", execptedDelayInSeconds=" + execptedDelayInSeconds
                + ", actualDelayInSeconds=" + actualDelayInSeconds);
        }
    }

}
