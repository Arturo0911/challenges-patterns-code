package com.company.solutions;

import java.util.Scanner;

public class RepeatedString {

    //private static final Scanner scanner = new Scanner(System.in);

    public RepeatedString(){}

    public static void main(String[] args) {

        String word = "abcac";
        String [] wordd = word.split("");
        String newString = "";
        int counter = 0;
        int number = 10;
        for (int i =0; i < number; i++){

            if (counter >= wordd.length){
                counter = 0;
                newString  =newString + wordd[counter];
                //newString  =newString + word.substring(0,counter);
            }else{
                newString  =newString + wordd[counter];
                //System.out.println(wordd[counter]);
            }

            counter++;
        }
        int sum =0;
        for (int j =0; j < number; j++){
            if (newString.charAt(j) == 'a'){
                sum++;
            }
        }

        System.out.println(sum);



        System.out.println(newString);
    }
}
