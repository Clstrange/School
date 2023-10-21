package com.codystrange.Project1;

public class Duck extends Animal {

    public Duck(String name, int age) {
        super(name, age, "Quack", "Papa Johns Pizza");
    }

    // Prints the sound of the animal
    @Override
    void makeSound() {
        System.out.println(this.getSound());
    }

}
