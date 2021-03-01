package com.company.process.interview;

import javax.json.Json;
import javax.json.JsonArray;
import javax.json.JsonObject;
import javax.json.JsonReader;
import java.net.*;
import java.io.*;
import java.util.*;


/**
 * @author Arturo Negreiros
 * @version Java 11
 */

public class RickAndMorty {

	// Rick and Morty API
	private static final String rickAndMortyApi = "https://rickandmortyapi.com/api/character";

	
	public RickAndMorty(){ }





	public void readRickAndMorty() throws MalformedURLException {

		URL url = new URL(rickAndMortyApi);
		try (InputStream inputStream =  url.openStream();
			 JsonReader jsonReader = Json.createReader(inputStream)) {

			JsonObject object = jsonReader.readObject();
			JsonArray jsonArray = object.getJsonArray("results");

			for (JsonObject results : jsonArray.getValuesAs(JsonObject.class)){
				System.out.println(results);
			}

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


	public static void main(String[] args)  {

		RickAndMorty api = new RickAndMorty();
		//api.readCovidPage();

		try {
			api.readRickAndMorty();

		}catch (MalformedURLException e ){
			e.printStackTrace();
			System.out.println(e.toString());
		}


	}


}