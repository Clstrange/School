package com.codystrange.javaoopone;

import java.util.Random;

public class StopWatchTester {
    public static void sort(int[] arr) {
        int n = arr.length;

        // Move boundary of unsorted array
        for (int i = 0; i < n - 1; i++) {
            // Find the minimum element in the unsorted array
            int min_idx = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[min_idx]) {
                    min_idx = j;
                }
            }

            // Swap the found minimum element with the first element
            int temp = arr[min_idx];
            arr[min_idx] = arr[i];
            arr[i] = temp;
        }
    }

    public static void main(String[] args) {
        Random rand = new Random();
        StopWatch timer = new StopWatch();
        timer.start();

        // Creating array of 100,000 random numbers range: 0-9
        int[] arr = new int[100000];
        for (int i = 0; i < 100000; i++) {
            int randomInt = rand.nextInt(10);
            arr[i] = randomInt;
        }

        sort(arr);
        timer.stop();
        System.out.println(timer.getElapsedTime());
    }
}

