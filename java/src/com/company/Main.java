package com.company;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Main {




/**
 *@param grid the matrix with the positions
 *@param n is bot position
 *
 * */
static void displayPathtoPrincess(int n, String [] grid){
    
    ArrayList<ArrayList<String>> vector = new ArrayList<ArrayList<String>>();
    int peachPositionW =  0;
    int peachPositionH =  0;
    int botPositionW = 0;
    int botPositionH = 0;
    int counter = 0;


        for (int x = 0; x < grid.length; x++){
            String [] source = grid[x].split("");
            ArrayList<String> values = new ArrayList<String>();
            for (int z = 1; z < source.length; z++){
                values.add(source[z]);
            }
            vector.add(values);
        }
    
    for (int i =0 ; i < vector.size(); i++){
            
            for (int j =0; j < vector.size(); j++){
                
                if (vector.get(i).get(j).equals("m")){
                    
                    botPositionW = j;
                    botPositionH = i;
                }else if (vector.get(i).get(j).equals("p")){

                    peachPositionW = j;
                    peachPositionH = i;
                }
            }
        }
    
    if (botPositionH > peachPositionH){
        counter = botPositionH - peachPositionH;
        
        for (int x = 0; x < counter; x++){
            System.out.println("UP");
        }
    } else if (botPositionH < peachPositionH){
        counter =  peachPositionH - botPositionH;
        
        for (int x = 0; x < counter; x++){
            System.out.println("DOWN");
        }
    }
    
    if (botPositionW > peachPositionW){
        counter = botPositionW - peachPositionW;
        
        for (int x = 0; x < counter; x++){
            System.out.println("LEFT");
        }
    } else if (botPositionW < peachPositionW){
        counter =  peachPositionW - botPositionW;
        
        for (int x = 0; x < counter; x++){
            System.out.println("RIGHT");
        }
    }
  }

public void countPositionBtwBotPeach (){}


public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int m;
        m = in.nextInt();
        String grid[] = new String[m];
        for(int i = 0; i < m; i++) {
            grid[i] = in.next();
        }

    displayPathtoPrincess(m,grid);
    }
}
