package com.codystrange.Project1;

public class Dog extends Animal {
    String sound;
    public Dog(String name, int age) {
        super(name, age);
        sound = "Woof!";
    }

    // Prints the sound of the animal
    @Override
    void makeSound() {
        System.out.println(sound);
    }

}
