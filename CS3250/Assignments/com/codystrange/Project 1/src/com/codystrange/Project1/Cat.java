package com.codystrange.Project1;
public class Cat extends Animal{
    String sound;
    public Cat(String name, int age) {
        super(name, age);
        sound = "Meow!";
    }

    // Prints the sound of the animal
    @Override
    void makeSound() {
        System.out.println(sound);
    }

}
