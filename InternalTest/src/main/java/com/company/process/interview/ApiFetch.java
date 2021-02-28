package com.company.process.interview;

import java.net.*;
import java.io.*;
import java.util.*;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

/**
 * @author Arturo Negreiros
 * @version Java 11
 */

public class ApiFetch {


	// Covid page 
	private static final String covidPage  = "https://covid19.who.int/WHO-COVID-19-global-data.csv";

	// Rick and Morty API
	private static final String rickAndMortyApi = "https://rickandmortyapi.com/api";


	private final ArrayList<String> covidCountries;

	private final ArrayList<String> covidDates;
	
	public ApiFetch(){

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



	public void readRickAndMorty(){

		/*
		 *
		 * Status code 200 means to -> the connection and the response is ok
		 *
		 *
		 * 
		 */

		try {
			String inLine = "";

			URL urlConnector  = new URL(rickAndMortyApi);
			// cast the URL object urlConnector to get her properties.
			HttpURLConnection connection = (HttpURLConnection) urlConnector.openConnection();
			connection.setRequestMethod("GET");
			int responseCode = connection.getResponseCode();

			if ( response == 200){
				System.out.println(responseCode);
				Scanner scanner = new Scanner(urlConnector.openStream());

				while(scanner.hasNext()){
					inLine += scanner.nextLine();
				}

			}else{

				System.out.println("Someting happend");
			}



			


		}catch(Exception e){

			e.printStackTrace();
			System.out.println(e.toString());
		} 


	}



	/**
	 * 
	 * TO-DO:
	 * 	- First read the data from the endpoint
	 */


	public static void main(String[] args){

		ApiFetch api = new ApiFetch();
		//api.readCovidPage();
		api.readRickAndMorty();



	}


}