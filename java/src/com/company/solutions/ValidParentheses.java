package com.company.solutions;

import javax.crypto.Mac;
import java.util.Stack;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ValidParentheses {


    public boolean isValid(String s){

        String [] patterns = s.split("");
        int size = patterns.length - 1;
        if (patterns.length <= 2) {
            Pattern pattern = Pattern.compile("\\(\\)|\\[\\]|\\{\\}");
            Matcher matcher = pattern.matcher(s);
            return matcher.find();
        }else if (patterns.length % 2 != 0){
            return false;
        }else{
            Pattern pattern = Pattern.compile("\\(\\{\\[\\]\\}\\)|\\(\\[\\{\\}\\]\\)|\\[\\(\\{\\}\\)\\]|\\[\\{\\(\\)\\}\\]|" +
                    "\\{\\[\\(\\)\\]\\}|\\{\\(\\[\\]\\)\\}|");
            Matcher matcher = pattern.matcher(s);
            return  matcher.find();
        }

    }

    public static void main(String[] args) {

        /*ValidParentheses valid = new ValidParentheses();
        String word = "()[]{}";
        System.out.println(valid.isValid(word));*/

        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i<= 5; i++){
            stack.push(i);
        }
        System.out.println(stack);
        stack.pop();
        System.out.println(stack);

    }
}
