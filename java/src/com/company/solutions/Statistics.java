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
        ArrayList<Integer> values = new ArrayList<>();
        scanner.nextLine();
        for (int x =0; x < size; x ++){
            values.add(scanner.nextInt());
        }

        System.out.println(values);
    }
}
