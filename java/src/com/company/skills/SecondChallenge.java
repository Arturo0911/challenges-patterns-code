package com.company.skills;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;



class Result {

    /*
     * Complete the 'maxCost' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER_ARRAY cost
     *  2. STRING_ARRAY labels
     *  3. INTEGER dailyCount
     */

    public static int maxCost(List<Integer> cost, List<String> labels, int dailyCount) {
        // Write your code here

        int counter1 = 0;
        int counter= 0;
        int maxSum = 0;


        while (true){

            for (int i=0; i < labels.size(); i++){




                if (dailyCount == counter){
                    for (int x =0; x < dailyCount; x++){

                    }
                }

                if (labels.get(i).equals("legal") && counter < dailyCount){
                    counter++;
                    maxSum += cost.get(i);
                }

            }

        }





        return maxSum;



    }

}

public class SecondChallenge {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int costCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> cost = IntStream.range(0, costCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine().replaceAll("\\s+$", "");
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
                .map(String::trim)
                .map(Integer::parseInt)
                .collect(toList());

        int labelsCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<String> labels = IntStream.range(0, labelsCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
                .collect(toList());

        int dailyCount = Integer.parseInt(bufferedReader.readLine().trim());

        int result = Result.maxCost(cost, labels, dailyCount);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}