

public class Main{

    public static void triangle(int height){
        for (int x=1; x <= height; x++){
            for (int y= 1; y <= x; y++){
                System.out.print("*    ");
            }
            System.out.println("");
        }
    }

    public static void main(String[] args){
        System.out.println("hello world");
        triangle(10);
    }
}
