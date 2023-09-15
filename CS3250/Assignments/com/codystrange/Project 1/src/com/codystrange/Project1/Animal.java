package com.codystrange.Project1;

abstract class Animal {
    // name: The animal's name
    private final String name;

    // age: The animal's age
    private final int age;

    // sound: The sound the animal makes (string)
    private String sound;

    // Constructor
    public Animal(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Prints the sound of the animal
    abstract void makeSound();

    // Prints the name and age of the animal
    public void displayInfo() {
        System.out.println("Name: " + this.name + "\nAge: " + this.age);
    };

    public String getName() {
        return this.name;
    }
}

