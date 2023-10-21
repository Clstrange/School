package com.codystrange.Project1;

abstract class Animal {
    // name: The animal's name
    private final String name;

    // age: The animal's age
    private final int age;

    // sound: The sound the animal makes (string)
    private final String sound;

    private final String favoriteFood;

    // Constructor
    public Animal(String name, int age, String sound, String favoriteFood) {
        this.name = name;
        this.age = age;
        this.sound = sound;
        this.favoriteFood = favoriteFood;
    }

    // Prints the sound of the animal
    abstract void makeSound();

    // Prints the name and age of the animal
    public void displayInfo() {
        System.out.println("Animal Name: " + this.name + "\nAge: " + this.age);
    };

    public String getName() {
        return this.name;
    }

    public String getSound() {
        return this.sound;
    }

    public String getFavoriteFood() {return this.favoriteFood;}
}

