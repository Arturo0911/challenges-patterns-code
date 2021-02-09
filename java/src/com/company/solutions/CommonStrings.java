package com.company.solutions;

import com.company.Main;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;

public class CommonStrings {

    /**
     * @param
     *
     *
     * */
    public String longestCommonPrefix(String[] strs) {
        int sizeString = strs.length;
        String param = "";
        ArrayList<Integer> vectorSize = new ArrayList<>();
        for (String wordSizes: strs){
            vectorSize.add(wordSizes.length());
        }
        Collections.sort(vectorSize);
        int commonSize = vectorSize.get(0);





        return null;
    }


    public static void main(String[] args) {
        CommonStrings common = new CommonStrings();
        String [] words = {"flower", "flow", "flautarin"};
        //System.out.println(common.longestCommonPrefix(words));

        String palabra = "Arturo";
        System.out.println(palabra.substring(0,5));


    }
}
