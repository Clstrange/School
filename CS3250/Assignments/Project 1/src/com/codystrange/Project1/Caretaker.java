package com.codystrange.Project1;

abstract class Caretaker {
    private String name;
    private String specialAbility;


    protected Caretaker(String name, String specialAbility) {
        this.name = name;
        this.specialAbility = specialAbility;
    }

    // An interaction between the caretaker and an animal.
    abstract void communicateWithAnimal();

    // Prints the name and special ability of the caretaker.
    public void describe() {
        System.out.println("Caretaker Name: "+ this.name +"\nSpecial Ability: " + this.specialAbility);
    }
}
