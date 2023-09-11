package com.codystrange.javaoopone;
// Test program
public class FanTester {
    public static void main(String[] args) {
        Fan fanOne = new Fan();
        Fan fanTwo = new Fan();

        fanOne.setSpeed(3);
        fanOne.setRadius(10);
        fanOne.setColor("yellow");
        fanOne.setOn(true);

        fanTwo.setSpeed(2);
        fanTwo.setRadius(5);
        fanTwo.setColor("blue");
        fanTwo.setOn(false);

        System.out.println(fanOne.toString() + '\n');
        System.out.println(fanTwo.toString());

    }
}
