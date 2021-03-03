package com.company.skills;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

/**
 * @author Arturo Negreiros
 */

public class ArraysTwoDimension {
    /*
     *
     * 1 1 1 0 0 0
     * 0 1 0 0 0 0
     * 1 1 1 0 0 0
     * 0 0 2 4 4 0
     * 0 0 0 2 0 0
     * 0 0 1 2 4 0
     */

    static int hourglassSum(int[][] arr) {

        ArrayList<Integer> finalSum = new ArrayList<>();

        for(int k =0; k < 3+1; k++){
            int sum =0;
            int position =0;
            for (int i =0; i < 3; i++){

                for (int j =k; j < 3+k; j++){

                    if (position == 1){
                        finalSum += arr[][];
                        position ++;
                        break;
                    }else{

                    }
                    position++;

                    System.out.print(arr[i][j]);
                }
                System.out.println("");
            }
            System.out.println("\n");
        }

        for(int k =0; k < 3+1; k++){
            int sum =0;
            for (int i =3; i < 6; i++){

                for (int j =k; j < 3+k; j++){
                    System.out.print(arr[i][j]);

                }
                System.out.println("");
            }
            System.out.println("\n");
        }

        Collections.sort(finalSum);
        return finalSum.get(finalSum.size() - 1);
    }


    public static void main(String[] args) throws IOException {

        //BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int[][] arr = new int[6][6];

        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < 6; i++) {
            String[] arrRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 6; j++) {
                int arrItem = Integer.parseInt(arrRowItems[j]);
                arr[i][j] = arrItem;
            }
        }

        int result = hourglassSum(arr);

        /*bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();*/

        scanner.close();

    }
}
