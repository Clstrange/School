package com.codystrange.Project1;

import com.codystrange.Project1.Dog;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        Animal test = new Dog("john", 12);
        test.displayInfo();
        test.makeSound();
        Caretaker test2 = new LordWoofers("Johnny");
        test2.describe();

        test2.prepareFood("Papa Johns Pizza");

        test2.feedAnimal(test);

    }
}