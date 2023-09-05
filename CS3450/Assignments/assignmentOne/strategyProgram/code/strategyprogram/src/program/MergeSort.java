package program;

import java.util.Collections;

public class MergeSort extends SortedList {
    public MergeSort(){
        super();
        sortType = "MergeSort";
    }

    @Override
    public void sort() {
        // 'sorts' the list according to the quicksort method
        Collections.sort(studentList);
    }
    
}
