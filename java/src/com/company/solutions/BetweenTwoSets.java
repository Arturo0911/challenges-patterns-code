package com.company.solutions;


import java.io.*;
import java.util.Collections;
import java.util.List;
import java.util.stream.Stream;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;


/**
 * @author Arturo Negreiros
 */
class NewResult {

    /*
     * Complete the 'getTotalX' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER_ARRAY a
     *  2. INTEGER_ARRAY b
     */

    public static boolean hasFactors(int number, List<Integer>arr){
        for(int i = 0; i < arr.size(); i++){
            if(number % arr.get(i) != 0) return false;
        }
        return true;
    }

    public static boolean isFactor(int number, List<Integer> arr){
        for(int j = 0; j < arr.size(); j++){
            if(arr.get(j) % number != 0) return false;
        }
        return true;
    }

    public static int getTotalX(List<Integer> a, List<Integer> b) {
        // Write your code here
        Collections.sort(a);
        Collections.sort(b);
        int counter = 0;
        int min = a.get(0);
        int max = b.get(b.size() - 1);

        for (int x = min; x < max; x++ ) {
            if(hasFactors(x, a) && isFactor(x, b)) counter ++;
        }


        return counter;

    }

}
public class BetweenTwoSets {

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);

        int m = Integer.parseInt(firstMultipleInput[1]);

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        List<Integer> brr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        int total = NewResult.getTotalX(arr, brr);

        bufferedWriter.write(String.valueOf(total));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }

}
