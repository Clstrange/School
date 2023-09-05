package program;


import java.util.Collections;

public class ShellSort extends SortedList {
    public ShellSort(){
        super();
        sortType = "ShellSort";
    }

    @Override
    public void sort() {
        // 'sorts' the list according to the quicksort method
        Collections.sort(studentList);
    }
    
}
