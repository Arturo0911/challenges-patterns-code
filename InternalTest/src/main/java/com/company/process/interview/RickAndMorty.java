package com.company.process.interview;

import java.net.*;
import java.io.*;
import java.util.*;


/**
 * @author Arturo Negreiros
 * @version Java 11
 */

public class RickAndMorty {


	// Covid page 
	private static final String covidPage  = "https://covid19.who.int/WHO-COVID-19-global-data.csv";

	// Rick and Morty API
	private static final String rickAndMortyApi = "https://rickandmortyapi.com/api/character";


	private final ArrayList<String> covidCountries;

	private final ArrayList<String> covidDates;
	
	public RickAndMorty(){

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



	public void readRickAndMorty()  {

		try {
			URL connector = new URL(rickAndMortyApi);
			BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(connector.openStream()));
			String inLines;
			int counter = 0;
			while((inLines  = bufferedReader.readLine()) != null){
				String[] lines = inLines.split(",");
				System.out.println(lines[counter]);
				counter++;
			}

			bufferedReader.close();


		}catch (MalformedURLException malformedURLException){
			malformedURLException.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}

	}



	/**
	 * 
	 * TODO -> Training to fetch data from any end point:
	 * 	- First read the data from the endpoint
	 */


	public static void main(String[] args){

		RickAndMorty api = new RickAndMorty();
		//api.readCovidPage();
		api.readRickAndMorty();



	}


}