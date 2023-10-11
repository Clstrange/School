package com.codystrange.InnerClassesGenericsAndCollections;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class Student {
    private String name;
    private int age;
    private double gpa;
    private final ArrayList<Student> students = new ArrayList<Student>();

    public Student(String name, int age, double gpa) {
        this.name = name;
        this.age = age;
        this.gpa = gpa;
    }

    public void createStudents() {
        Student s1 = new Student("John", 13, 3.75);
        Student s2 = new Student("James", 15, 2.15);
        Student s3 = new Student("Jim", 18, 4.0);
        students.add(s1);
        students.add(s2);
        students.add(s3);
    }

    public void sortStudentsByGPADescending() {
        Collections.sort(students, new Comparator<Student>() {
            @Override
            public int compare(Student s1, Student s2) {
                return Double.compare(s1.gpa, s2.gpa);
            }
        });
    }

    public void displayStudents() {
        for (Student student: students
        ) {
            System.out.println(student.name + "GPA: " + student.gpa);

        }
    }
}