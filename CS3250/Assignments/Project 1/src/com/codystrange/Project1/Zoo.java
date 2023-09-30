package com.codystrange.Project1;

import java.util.ArrayList;

public class Zoo implements ZooOperations{
    // uses an ArrayList to manage and store the collection of animals.
    ArrayList<Animal> animalList;
    ArrayList<Exhibit> exhibitList;

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

    // Methods to add, remove, and list exhibits.
    @Override
    public void addExhibit(Exhibit exhibit) {
        exhibitList.add(exhibit);
    }

    @Override
    public void removeExhibit(String name) {
        this.exhibitList.removeIf(exhibit -> exhibit.getName().equals(name));
    }

    @Override
    public void listExhibit() {
        for (Exhibit exhibit: this.exhibitList
        ) {
            System.out.println(exhibit.getName());
        }
    }

    public static class Exhibit {
        private String name;
        private String description;
        private final ArrayList<Animal> animals;

        public Exhibit(String name, String description, ArrayList<Animal> animals) {
            this.name = name;
            this.description = description;
            this.animals = animals;
        }

        // Adds an animal to this exhibit.
        public void addAnimalToExhibit(Animal animal) {
            animals.add(animal);
        }

        // Removes an animal from this exhibit.
        public void removeAnimalFromExhibit(String name) {
            this.animals.removeIf(animal -> animal.getName().equals(name));
        }

        // Lists all the animals in the exhibit.
        public void listAnimalsInExhibit() {
            for (Animal animal:this.animals
                 ) {
                System.out.println(animal.getName());

            }
        }

        public String getName() {
            return this.name;
        }

        public String getDescription() {
            return this.description;
        }

    }
}
