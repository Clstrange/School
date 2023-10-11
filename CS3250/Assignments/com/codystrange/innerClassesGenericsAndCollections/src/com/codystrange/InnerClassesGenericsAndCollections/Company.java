package com.codystrange.InnerClassesGenericsAndCollections;

import java.util.ArrayList;
import java.util.Iterator;

public class Company {
    private ArrayList<Employee> employees = new ArrayList();

    public Company() {
    }

    public void addEmployee(String name, int employeeID, double salary) {
        this.employees.add(new Employee(name, employeeID, salary));
    }

    public void calculateTotalSalary() {
        double totalSalary = 0.0;

        Employee employee;
        for(Iterator var3 = this.employees.iterator(); var3.hasNext(); totalSalary += employee.salary) {
            employee = (Employee)var3.next();
        }

        System.out.println("Total salary of all employees is: " + totalSalary);
    }

    public static class Employee {
        private final String name;
        private int employeeID;
        private double salary;

        public Employee(String name, int employeeID, double salary) {
            this.name = name;
            this.employeeID = employeeID;
            this.salary = salary;
        }
    }
}
