package com.codystrange.Project1;

public class Dog extends Animal {

    public Dog(String name, int age) {
        super(name, age, "Woof");
    }

    // Prints the sound of the animal
    @Override
    void makeSound() {
        System.out.println(this.getSound());
    }

}
