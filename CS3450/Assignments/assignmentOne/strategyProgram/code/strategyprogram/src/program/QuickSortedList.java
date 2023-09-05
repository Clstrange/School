package program;

import java.util.Collections;

public class QuickSortedList extends SortedList {
    public QuickSortedList(){
        super();
        sortType = "QuickSort";
    }

    @Override
    public void sort() {
        // 'sorts' the list according to the quicksort method
        Collections.sort(studentList);
    }
    
}
