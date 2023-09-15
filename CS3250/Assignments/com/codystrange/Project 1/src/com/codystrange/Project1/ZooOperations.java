package com.codystrange.Project1;

public interface ZooOperations {
    // addAnimal(Animal): adds an animal to the zoo
    public void addAnimal(Animal animal);

    // removeAnimal(name): removes an animal from the zoo based on its name
    public void removeAnimal(String name);

    // listAnimals(): lists all the animals currently in the zoo
    public void listAnimal();
}
