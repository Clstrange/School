package com.codystrange.Project1;
public class Cat extends Animal{

    public Cat(String name, int age) {
        super(name, age, "Meow", "Sirloin Steak");
    }

    // Prints the sound of the animal
    @Override
    void makeSound() {
        System.out.println(this.getSound());
    }

}
