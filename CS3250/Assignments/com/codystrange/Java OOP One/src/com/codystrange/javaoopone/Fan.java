package com.codystrange.javaoopone;

public class Fan {
    private static final int SLOW = 1;
    private static final int MEDIUM = 2;
    private static final int FAST = 2;
    private int speed;
    private boolean on;
    private double radius;
    private String color;

    // A no-arg constructor that creates a default fan.
    public Fan() {
        this.speed = SLOW;
        this.on = false;
        this.radius = 5;
        this.color = "blue";
    }

    // The accessor and mutator methods for all four data fields.
    public int getSpeed() {
        return speed;
    }

    public double getRadius() {
        return radius;
    }

    public String getColor() {
        return color;
    }

    public boolean getOn() {
        return on;
    }

    public void setOn(boolean on) {
        this.on = on;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }

    // returns a string description for the fan
    @Override
    public String toString() {
        String description;
        if (this.on) {
            description = "Fan Speed: " + this.speed
                    + "\nFan Color: " + this.color
                    + "\nFan Radius: " + this.radius;
        }
        else {
            description = "Fan Color: " + this.color
                    + "\nFan Radius: " + this.radius
                    + "\nFan is off";
        }
        return description;
    }
}
