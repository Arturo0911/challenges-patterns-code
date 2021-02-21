package com.process;

public class Main {

    public static void main(String[] args) {

        ListProcess.vehiculoLista.add(new Vehicle("002455", "Chevrolet", "trail",
                "2019", "Rojo", "Arturo", "Negreiros",
                "0918237421", "limpieza", "wash"));
        ListProcess.vehiculoLista.add(new Vehicle("457878", "Mazda", "negro",
                "2019", "gris", "juan", "Samanez",
                "4645645646", "Pintado", "painting"));


        System.out.println(ListProcess.vehiculoLista.get(0).getMarca());

        for (Vehicle vehicle : ListProcess.vehiculoLista){
            System.out.println(vehicle);
        }

    }
}
