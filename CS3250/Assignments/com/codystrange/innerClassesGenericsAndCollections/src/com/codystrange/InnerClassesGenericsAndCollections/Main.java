package com.codystrange.InnerClassesGenericsAndCollections;

import java.io.PrintStream;
import java.lang.reflect.Array;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Student poorlyNamedClass = new Student("pointless", 95,10.12);
        poorlyNamedClass.createStudents();
        poorlyNamedClass.displayStudents();
        System.out.println("\n\n");
        poorlyNamedClass.sortStudentsByGPADescending();
        poorlyNamedClass.displayStudents();

    }
}
