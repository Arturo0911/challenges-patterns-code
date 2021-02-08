package com.company.solutions;

import com.company.Main;

public class Solution {
    public static int[] twoSum(int[] nums, int target) {
        int size = nums.length;
        for (int x = 0; x < size;x++ ){
            for(int i =0; i < size; i++) {

                while(x != i){
                    if (nums[x] + nums[i] == target){
                        return new int[] {x,i};

                    }else{
                        break;
                    }

                }
            }

        }
        return null;

    }

    public static void main(String[] args) {

        Main main = new Main();

        int[] values = {3,2,4};

        for (int value : twoSum(values, 6)){
            System.out.print(value);
        }

    }
}
