package com.company.solutions;

public class IsPalindrome {
    /*public static boolean isPalindrome(int x) {

        String numberFinal = "";
        int comparationNumber = x;
        if (x < 0){
            return false;
        }else{
            while(x % 10 != 0){
                int res = x%10;
                x = x/10;
                numberFinal += res ;
            }
            return comparationNumber == Integer.parseInt(numberFinal);
        }


    }*/

    public static void main(String[] args) {
        //System.out.println(isPalindrome(121));
        //System.out.println(isPalindrome(-121));
        int number = 12321;
        System.out.println("number before process: "+number);
        int reverseNumber= 0;

        while (number != 0){
            reverseNumber = reverseNumber * 10 + number%10;
            number /=10;
        }

        System.out.println("number after process"+reverseNumber);


    }



}
