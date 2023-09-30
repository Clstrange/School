package com.codystrange.Project1;

public class DemonDuckExorcist extends Caretaker{

    public DemonDuckExorcist(String name) {
        super(name, "Holy Cleanse");
    }

    // An interaction between the caretaker and an animal.
    @Override
    void communicateWithAnimal() {
        System.out.println("The DemonDuckExorcist casts the Holy Cleanse ritual to exorcise the demonic spirits " +
                "that the duck has manifested");
    }
}
