package program;

import java.util.ArrayList;

public abstract class SortedList {
    protected ArrayList<String> studentList = new ArrayList<>();
    protected String sortType;

    public SortedList() {
    }

    public void add(String studentName) {
        studentList.add(studentName);
    }
    public void delete(String studentName) {
        studentList.remove(studentName);
    }

    public void display() {
        for (String studentName:studentList) {
            System.out.print(studentName + '\n');
        }
        System.out.print('\n');
    }

    abstract public void sort();
}
