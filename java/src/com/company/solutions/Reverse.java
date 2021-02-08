package com.company.solutions;

public class Reverse {
    public static int reverse(int x) throws NumberFormatException {
        String finalnNumber = "";
        //int final =0;
        if (x < 0 ){
            x = (-1) * x;
            while (x%10!=0){
                int res =x%10;
                x = x /10;
                finalnNumber += res;

            }
            //int final = Integer.parseInt(finalnNumber);
            return ((-1) * Integer.parseInt(finalnNumber));
        }else{
            while (x%10!=0){
                int res =x%10;
                x = x /10;
                finalnNumber += res;

            }

            return Integer.parseInt(finalnNumber);
        }



    }


    public static void main(String[] args) {
        System.out.println(reverse(-321));
        String [] values = {};
        //System.out.println(3 /10  );
    }
}
