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

        if (strs.length == 0) return "";

        String prefix = strs[0];

        for (int i = 1; i < strs.length; i++){

            while(strs[i].indexOf(prefix) != 0){
                prefix = prefix.substring(0, prefix.length() - 1);
                if (prefix.isEmpty())return "";
            }

        }
        return prefix;
    }


    public static void main(String[] args) {
        CommonStrings common = new CommonStrings();
        String [] words = {"flower", "flow", "flight"};

        String letter = words[0];
        //System.out.println(common.longestCommonPrefix(words));

        System.out.println(words[1].substring(4,4));

        System.out.println(words[1].indexOf(letter));

    }
}
