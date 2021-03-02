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

/**
 * @author  Arturo Negreiros
 */

class Result {

    /*
     * Complete the 'findSum' function below.
     *
     * The function is expected to return a LONG_INTEGER_ARRAY.
     * The function accepts following parameters:
     *  1. INTEGER_ARRAY numbers
     *  2. 2D_INTEGER_ARRAY queries
     */

    public static List<Long> findSum(List<Integer> numbers, List<List<Integer>> queries) {
        // Write your code here
        List<Long> longResult = new ArrayList<>();
        int  suma =0 ;
        for(List<Integer> vectors: queries){

            if( (numbers.get(vectors.get(0) - 1) + numbers.get(vectors.get(1) - 1)) % 10  == 0 ){
                suma += (numbers.get(vectors.get(0) - 1) + numbers.get(vectors.get(1) - 1)) + vectors.get(2) ;
                Long data = new Long(suma);
                longResult.add(data);
            }else{
                suma += (numbers.get(vectors.get(0) - 1) + numbers.get(vectors.get(1) - 1));
                Long data = new Long(suma);
                longResult.add(data);
            }

        }

        return  longResult;

    }

}

public class Skills {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int numbersCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> numbers = IntStream.range(0, numbersCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine().replaceAll("\\s+$", "");
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
                .map(String::trim)
                .map(Integer::parseInt)
                .collect(toList());

        int queriesRows = Integer.parseInt(bufferedReader.readLine().trim());
        int queriesColumns = Integer.parseInt(bufferedReader.readLine().trim());

        List<List<Integer>> queries = new ArrayList<>();

        IntStream.range(0, queriesRows).forEach(i -> {
            try {
                queries.add(
                        Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                                .map(Integer::parseInt)
                                .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        List<Long> result = Result.findSum(numbers, queries);

        bufferedWriter.write(
                result.stream()
                        .map(Object::toString)
                        .collect(joining("\n"))
                        + "\n"
        );

        bufferedReader.close();
        bufferedWriter.close();
    }
}
