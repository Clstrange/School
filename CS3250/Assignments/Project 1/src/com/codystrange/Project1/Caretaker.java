package com.codystrange.Project1;

import java.util.ArrayList;

abstract class Caretaker {
    private final String name;
    private final String specialAbility;

    private FeedingBucket bucket;


    protected Caretaker(String name, String specialAbility) {
        this.name = name;
        this.specialAbility = specialAbility;
    }

    static class FeedingBucket {
        ArrayList<String> foodItems;

        public FeedingBucket() {
            foodItems = new ArrayList<String>();

        }

        public void addFood(String food) {
            foodItems.add(food);
        }

        public void removeFood(String food) {
            foodItems.remove(food);
        }

        public void listFoods() {
            for (String food: foodItems
                 ) {
                System.out.println(food + "\n");

            }
        }

    }

    // An interaction between the caretaker and an animal.
    abstract void communicateWithAnimal();

    // Prints the name and special ability of the caretaker.
    public void describe() {
        System.out.println("Caretaker Name: "+ this.name +"\nSpecial Ability: " + this.specialAbility);
    }

    public void prepareFood(String food) {
        bucket.addFood(food);
    }

    public String feedAnimal(Animal a) {
        for (String food: bucket.foodItems
             ) {

            if (a.getFavoriteFood().equals(food)) {
                bucket.removeFood(food);
                System.out.println("Animal " + a.getName() + " has been fed");
                return "Animal " + a.getName() + " has been fed";
            }

        }
        System.out.println(a.getName() + " favorite food cannot be found.");
        return a.getName() + " favorite food cannot be found.";

    }


}
