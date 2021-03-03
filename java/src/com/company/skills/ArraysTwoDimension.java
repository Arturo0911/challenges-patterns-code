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
        for(int l =0; l < 4; l++){
            for(int k =0; k < 3+1; k++){
                int sum =0;
                int position =0;
                for (int i =l; i < 3+l; i++){

                    for (int j =k; j < 3+k; j++){

                        if (position == 1){
                            //System.out.print(arr[i][j+1]);
                            sum += arr[i][j+1];
                            //position ++;
                            break;
                        }else{
                            //System.out.print(arr[i][j]);
                            sum += arr[i][j];
                        }
                    }
                    position++;
                    //System.out.println("");
                }
                finalSum.add(sum);
                //System.out.println("\n");
            }
        }

        Collections.sort(finalSum);
        System.out.println(finalSum);
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

        System.out.println(result);

        /*bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();*/

        scanner.close();

    }
}
