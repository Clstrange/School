package com.codystrange.Project1;

public class LordWoofers extends Caretaker{

    public LordWoofers(String name) {
        super(name, "The Great WOOF!");
    }

    // An interaction between the caretaker and an animal.
    @Override
    void communicateWithAnimal() {
        System.out.println("The LordWoofers commands the dog to stop barking at tourists and through " +
                "the use of 'The Great WOOF!' The dog has no choice to obey");
    }
}
