package com.codystrange.Project1;

import java.util.ArrayList;

public class Zoo implements ZooOperations{
    // uses an ArrayList to manage and store the collection of animals.
    ArrayList<Animal> animalList;

    public Zoo() {
        this.animalList = new ArrayList<Animal>();
    }

    // addAnimal(Animal): adds an animal to the zoo
    @Override
    public void addAnimal(Animal animal) {
        this.animalList.add(animal);
    }

    // removeAnimal(name): removes an animal from the zoo based on its name
    @Override
    public void removeAnimal(String name) {
        this.animalList.removeIf(animal -> animal.getName().equals(name));
    }

    // listAnimals(): lists all the animals currently in the zoo
    @Override
    public void listAnimal() {
        for (Animal animal: this.animalList
             ) {
            System.out.println(animal.getName());
        }

    }
}
