package com.company.process.interview;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import java.net.*;
import java.io.*;


/**
 * @author Arturo Negreiros
 * @version Java 11
 */

public class RickAndMorty {

	// Rick and Morty API
	private static final String rickAndMortyApi = "https://rickandmortyapi.com/api/character";

	
	public RickAndMorty(){ }



	public void readFromUrlRickAndMorty() throws  Exception{

		URL url = new URL(rickAndMortyApi);
		HttpURLConnection httpURLConnection = (HttpURLConnection) url.openConnection();
		httpURLConnection.setRequestMethod("GET");

		if(httpURLConnection.getResponseCode() == 200){
			BufferedReader bufferedReader = new BufferedReader(new InputStreamReader( httpURLConnection.getInputStream(),"utf-8"));
			StringBuilder response = new StringBuilder();
			String inputLine; // this one gonna read each lines from the request
			while((inputLine = bufferedReader.readLine()) != null){
				response.append(inputLine);
			}
			bufferedReader.close();
			//System.out.println(response.toString());
			JSONParser jsonParser = new JSONParser(); // using the simple json library to change from string to json
			JSONObject jsonObject = (JSONObject) jsonParser.parse(response.toString());
			System.out.println(jsonObject);

		}else {
			System.out.println("error getting the data from the url ");
		}

	}



	/*public void readRickAndMorty() throws MalformedURLException {

		URL url = new URL(rickAndMortyApi);
		try (InputStream inputStream =  url.openStream();
			 JsonReader jsonReader = Json.createReader(inputStream)) {

			JsonObject object = jsonReader.readObject();
			System.out.println(object.getJsonObject("info"));
			String name = "arturo";

			System.out.println(name.substring(0,5));


		}catch (MalformedURLException malformedURLException){
			malformedURLException.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}

	}*/



	/**
	 * 
	 * TODO -> Training to fetch data from any end point:
	 * 	- First read the data from the endpoint
	 */


	public static void main(String[] args)  {

		RickAndMorty api = new RickAndMorty();

		try {
			api.readFromUrlRickAndMorty();
		}catch (Exception e ){
			e.printStackTrace();
			System.out.println(e.toString());
		}

	}


}