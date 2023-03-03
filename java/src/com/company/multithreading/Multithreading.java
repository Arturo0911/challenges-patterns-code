
import java.util.HashMap;


public class Multithreading {

    public static void main(String[] args) {
        HashMap<Object, Object> directions = new HashMap<>();
        directions.put("name", "Arturo");
        directions.put("lname", "Negreiros");
        System.out.println(directions);

        System.out.println(directions.get("name"));

        directions.remove("lname");
        System.out.println(directions);

        System.out.println(directions.get("lname"));

    }
}
