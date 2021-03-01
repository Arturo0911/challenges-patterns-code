package com.company.process.interview;


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.ArrayList;

public class CovidAPI {

    // Covid page
    private static final String covidPage  = "https://covid19.who.int/WHO-COVID-19-global-data.csv";
    private final ArrayList<String> covidCountries;
    private final ArrayList<String> covidDates;

    public CovidAPI(){
        this.covidCountries = new ArrayList<>();
        this.covidDates = new ArrayList<>();
    }

    public void readCovidPage(){

        try {

            URL urlReader = new URL(covidPage);
            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(urlReader.openStream())

            );

            String inputLine;
            //System.out.println(urlReader);

            while((inputLine = reader.readLine()) != null){
                String [] lines = inputLine.split(",");

                if (!covidCountries.contains(lines[2])){
                    covidCountries.add(lines[2]);
                }
                covidDates.add(lines[0]);
            }

            covidDates.remove(0);
            covidCountries.remove(0);

            reader.close();

            //System.out.println(covidCountries);

            for (String country: covidCountries){
                System.out.println(country);
            }

        }catch(Exception e ){
            e.printStackTrace();
            System.out.println(e.toString());
        }
    }
}
