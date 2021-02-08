package com.company.solutions;

import java.util.HashMap;

public class RomanNumber {

    HashMap<Character, Integer> romansNumber  = new HashMap<>(){

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

    /**
     * @param s the roman number
     *
     * */
    public int romanToInt(String s) {

        //int sizeNumber= romansNumber.get(s.charAt(0));
        HashMap<Character, Integer> romansNumber  = new HashMap<>(){

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

        int finalNumber = romansNumber.get(s.length() - 1);
        for (int i = s.length() - 1; i > 0; i--){

            if(romansNumber.get(s.charAt(i-1)) < romansNumber.get(s.charAt(i)) ){
                finalNumber -= romansNumber.get(s.charAt(i-1));
            }else{
                finalNumber += romansNumber.get(s.charAt(i-1));
            }

        }


        return finalNumber;
    }

    public static void main(String[] args) {
        RomanNumber roman = new RomanNumber();
        
    }

    /*public static void main(String[] args){
        System.out.println(romanToInt("XX"));

    }*/




}
