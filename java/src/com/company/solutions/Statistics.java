package com.company.solutions;

import java.util.ArrayList;
import java.util.Scanner;

public class Statistics {

    public static final Scanner scanner = new Scanner(System.in);


    /**
     * TODO:
     *      --  In this challenge, we practice calculating the mean,
     *              median, and mode.
     *      --  The first line contains the size of the array
     */
    public static void main(String[] args) {

        int size = scanner.nextInt();
        int sum = 0;
        float median = 0;
        float mean = 0;
        float mode = 0;
        ArrayList<Integer> values = new ArrayList<>();
        scanner.nextLine();
        String []arrays = scanner.nextLine().split(" ");

        for (String array: arrays){
            values.add(Integer.parseInt(array));
        }

        for (Integer value: values){
            sum += value;
        }
        mean = (float)(sum / size);

        System.out.printf("%.2f", ((float)(sum/size)));



        System.out.println(values);
    }
}
