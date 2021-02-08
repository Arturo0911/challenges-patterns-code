package com.company.solutions;

import java.util.HashMap;

public class RomanNumber {

    public static HashMap<Character, Integer> romansNumber  = new HashMap<>(){

        {
            put('I', 1);
            put('V', 5);
            put('X', 10);
            put('L', 50);
            put('C', 100);
            put('D', 500);
            put('M', 1000);

        }
    };

    public static int romanToInt(String s) {

        //int sizeNumber= romansNumber.get(s.charAt(0));
        int finalNumber = 0;//romansNumber.get(s.charAt(0));
        for (int i =0; i < s.length()-1; i++){
            if(romansNumber.get(s.charAt(i))> romansNumber.get(s.charAt(i + 1)) ){
                finalNumber += romansNumber.get(s.charAt(i));

            }else if (romansNumber.get(s.charAt(i)) == romansNumber.get(s.charAt(i + 1)) ){
                finalNumber += romansNumber.get(s.charAt(i));
            } else{
                finalNumber += romansNumber.get(s.charAt(i)) - 1;
            }
        }
        return finalNumber;
    }

    public static void main(String[] args){
        System.out.println(romanToInt("XX"));
    }



}
