package com.codystrange.Project1;

public class Duck extends Animal {
    String sound;
    public Duck(String name, int age) {
        super(name, age);
        sound = "Quack!";
    }

    // Prints the sound of the animal
    @Override
    void makeSound() {
        System.out.println(sound);
    }

}
