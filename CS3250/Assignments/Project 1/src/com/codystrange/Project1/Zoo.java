package com.codystrange.Project1;

import java.util.*;

public class Zoo<T extends Animal> implements ZooOperations{
    // uses an ArrayList to manage and store the collection of animals.
    Set<T> animalList;
    ArrayList<Exhibit<T>> exhibitList;

    Map<Caretaker, Set<T>> animalToCaretaker;

    public Zoo() {
        this.animalList = new HashSet<T>();
        animalToCaretaker = new HashMap<Caretaker, Set<T>>();
    }

    public void assignAnimalToCaretaker(Caretaker zk, T a) {
        if (animalToCaretaker.containsKey(zk)) {
            animalToCaretaker.get(zk).add(a);
        }
        else {
            animalToCaretaker.put(zk,new HashSet<T>());
        }
    }

    public void removeAnimalFromCaretaker(Caretaker zk, T a) {
        if (animalToCaretaker.containsKey(zk)) {
            animalToCaretaker.get(zk).remove(a);
        }
        else {
            System.out.println("No animal to remove");
        }
    }

    public Set<T> getAnimalsByCaretaker(Caretaker zk) {
        return animalToCaretaker.get(zk);
    }

    public T getAnimalsByFilter(String filter, String search) {
        if (filter.equals("name")) {
            for (T animal: animalList
                 ) {
                if (animal.getName().equals(search)) {
                    return animal;
                }

            }
            System.out.println("ERROR, no animal found");
            return null;
        } else if (filter.equals("sound")) {
            for (T animal: animalList
            ) {
                if (animal.getSound().equals(search)) {
                    return animal;
                }

            }
            System.out.println("ERROR, no animal found");
            return null;
        }
        System.out.println("Filter options are: name, sound");
        return null;
    }

    // addAnimal(Animal): adds an animal to the zoo
    public void addAnimal(T animal) {
        this.animalList.add(animal);
    }

    public int getAnimalCount() {
        return animalList.size();
    }

    // removeAnimal(name): removes an animal from the zoo based on its name
    @Override
    public void removeAnimal(String name) {
        this.animalList.removeIf(animal -> animal.getName().equals(name));
    }

    // listAnimals(): lists all the animals currently in the zoo
    @Override
    public void listAnimal() {
        for (T animal: this.animalList
             ) {
            System.out.println(animal.getName());
        }

    }

    // Methods to add, remove, and list exhibits.
    public void addExhibit(Exhibit<T> exhibit) {
        exhibitList.add(exhibit);
    }

    @Override
    public void removeExhibit(String name) {
        this.exhibitList.removeIf(exhibit -> exhibit.getName().equals(name));
    }

    @Override
    public void listExhibit() {
        for (Exhibit<T> exhibit: this.exhibitList
        ) {
            System.out.println(exhibit.getName());
        }
    }

    public static class Exhibit<T extends Animal> {
        private final String name;
        private final String description;
        private final ArrayList<T> animals;

        public Exhibit(String name, String description, ArrayList<T> animals) {
            this.name = name;
            this.description = description;
            this.animals = animals;
        }

        // Adds an animal to this exhibit.
        public void addAnimalToExhibit(T animal) {
            animals.add(animal);
        }

        // Removes an animal from this exhibit.
        public void removeAnimalFromExhibit(String name) {
            this.animals.removeIf(animal -> animal.getName().equals(name));
        }

        // Lists all the animals in the exhibit.
        public void listAnimalsInExhibit() {
            for (T animal:this.animals
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
