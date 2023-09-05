/*
Basics - Exercise 1
Name: John Doe
Description: Calculate and interpret BMI
 */

import java.util.Scanner;
import java.lang.Math;

public class CalculateAndInterpretBMI
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        // Constants
        final double KILOGRAMS_PER_POUND = 0.45359237;
        final double METERS_PER_INCH = 0.0254;

        // TODO: Prompt the user to enter weight in pounds
        System.out.print("Please enter your weight in pounds: ");
        double weight =  Double.parseDouble((input.nextLine()));

        // TODO: Prompt the user to enter height in inches
        System.out.print("Please enter your height in inches: ");
        double height =  Double.parseDouble((input.nextLine()));

        double bmi = ComputeBMI(weight, height);

        String bmiInterpretation = InterpretBMI(bmi);

        // Display result and interpretation
        System.out.println("BMI is " + bmi);
        System.out.println(bmiInterpretation);
    }

    public static double ComputeBMI(double weight, double height)
    {
        // TODO: Convert weight to kg and height to meters
        double weightInKg = weight * 0.45359237;
        double heightinM = height * 0.0254;

        // TODO: Compute BMI based on weight and height
        double bmi = weightInKg/(heightinM * heightinM);

        return bmi;
    }

    public static String InterpretBMI(double bmi)
    {
        /*
        TODO:
            return the following strings:
                "Underweight" if bmi is less than 18.5
                "Normal" if bmi is at least 18.5 but less than 25
                "Overweight" if bmi is at least 25 but less than 30
                "Obese" if bmi is greater than 30
         */

        if (bmi < 18.5) {
            return("Underweight");
        } else if (bmi >= 18.5 && bmi < 25) {
            return("Normal");
        } else if (bmi >=25 && bmi < 30) {
            return("Overweight");
        } else {
            return("Obese");
        }

    }


}
