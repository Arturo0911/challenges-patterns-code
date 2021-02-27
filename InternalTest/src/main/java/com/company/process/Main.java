package com.company.process;

import java.sql.Struct;
import java.util.*;

/**
 * @author  Arturo Negreiros
 */
public class Main {

    private HashMap<String, Object> socialMediaA = new HashMap<String,Object>();
    private HashMap<String, Object> socialMediaB = new HashMap<String,Object>();
    private HashMap<String, Object> socialMediaC = new HashMap<String,Object>();
    private ArrayList<HashMap> usersAndFollowers;



    public Main(){

        this.socialMediaA.put("User", "userA");
        this.socialMediaA.put("Following", new ArrayList<>(Arrays.asList("userB", "userD","userE", "userG")));
        this.socialMediaB.put("User", "userB");
        this.socialMediaB.put("Following", new ArrayList<>(Arrays.asList("userC", "userJ","userI", "userE")));
        this.socialMediaC.put("User", "userC");
        this.socialMediaC.put("Following", new ArrayList<>(Arrays.asList("userM", "userN","userJ", "userI", "userE")));

        this.usersAndFollowers = new ArrayList<HashMap>(Arrays.asList(this.socialMediaA, this.socialMediaB, this.socialMediaC));
    }

    public boolean verifyUsers(String usersFrom, String usersTo){

        try {
            return (socialMediaA.get("User").equals(usersFrom) || socialMediaB.get("User").equals(usersFrom) || socialMediaC.get("User").equals(usersFrom)) &&
                   ( socialMediaA.get("User").equals(usersTo) || socialMediaB.get("User").equals(usersTo) || socialMediaC.get("User").equals(usersTo));

        }catch (Exception e ){
            e.printStackTrace();
            return false;
        }

    }
    /**
     *
     * @param social
     * @param userStart
     * @param userDestiny
     * @param argument
     * @return integer(distance between the userInit to userDestiny
     */
    public int calculateFollowers(ArrayList<HashMap> social, String userStart, String userDestiny, String argument){

        /*
        *
        * * { “user”: “userA”,  “Following”: [“userB”, “userD”,“userE”, "userG"] }
         *
         * { “user”: “userB”,  “Following”: [“userC”, “userJ”,“userI”, "userE"] }
         *
         * { “user”: “userC”,  “Following”: [“userM”, “userN”,“userJ”, "userI", "userE"] }
         *
         * SI requiero a distancia entre "userA" y "userM"
        * */

        int counter = 0 ;
        int roadmapToUser = 0;
        String whoFollowUser = "";
        ArrayList<String> users = new ArrayList<String>();
        try {

            if(verifyUsers(userStart, userDestiny)){

                for (HashMap value : this.usersAndFollowers){
                    if(value.get("User").equals(userStart)){
                        for(String data : (List<String>)value.get("Following")){
                            continue;
                        }
                    }

                    if ( ( (List<String>)value.get("Following")).contains(userDestiny)){
                        System.out.println(value.get("User"));
                        users.add((String)value.get("User"));
                        counter ++;
                    }
                }
                System.out.println("The follow users "+users+" contains to "+userDestiny);
                System.out.println();

            }
            return 0;


        }catch (Exception e){
            e.printStackTrace();
            return  0;
        }

    }




    public static void main(String[] args) {

        Main main = new Main();
        System.out.println(main.verifyUsers("userA", "userB"));

        System.out.println(main.calculateFollowers(main.usersAndFollowers, "userA", "userB", "Following"));

    }
}
