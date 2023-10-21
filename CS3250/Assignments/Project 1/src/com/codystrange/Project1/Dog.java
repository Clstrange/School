package com.codystrange.Project1;

public class Dog extends Animal {

    public Dog(String name, int age) {
        super(name, age, "Woof", "Crispy Noodle Curry");
    }

    // Prints the sound of the animal
    @Override
    void makeSound() {
        System.out.println(this.getSound());
    }

}
