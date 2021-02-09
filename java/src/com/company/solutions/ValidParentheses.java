package com.company.solutions;

import javax.crypto.Mac;
import java.util.Stack;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ValidParentheses {

    /**
     * @param s the string with {}[]() as value or mixed
     * */
    public boolean isValid(String s){

        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++){
            if (s.charAt(i) == '(' ||s.charAt(i) == '['|| s.charAt(i) == '{' ){
                stack.push(s.charAt(i));
                continue;
            }

            if (stack.isEmpty()) return false;
            char check;
            switch (s.charAt(i)){
                case ')':
                    check = stack.pop();

                    if (check == '{' || check == '[')return false;
                        break;
                case '}':
                    check = stack.pop();
                    if (check == '(' || check == '[')return false;
                    break;
                case ']':
                    check = stack.pop();

                    if (check == '(' || check == '{')return false;
                    break;
            }
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {

        ValidParentheses valid = new ValidParentheses();
        String word = "{[]}";
        System.out.println(valid.isValid(word));

    }
}
