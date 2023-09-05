package program;


public class Main {
    public static void main(String[] args) {
        System.out.println("QuickSorted list");
        MergeSort studentListOne = new MergeSort();
        studentListOne.add("Anna");
        studentListOne.add("Jimmy");
        studentListOne.add("Samuel");
        studentListOne.add("Sandra");
        studentListOne.add("Vivek");
        studentListOne.display();


        System.out.println("ShellSorted list");
        MergeSort studentListTwo = new MergeSort();
        studentListTwo.add("Anna");
        studentListTwo.add("Jimmy");
        studentListTwo.add("Samuel");
        studentListTwo.add("Sandra");
        studentListTwo.add("Vivek");
        studentListTwo.display();

        System.out.println("MergeSorted list");
        MergeSort studentListThree = new MergeSort();
        studentListThree.add("Anna");
        studentListThree.add("Jimmy");
        studentListThree.add("Samuel");
        studentListThree.add("Sandra");
        studentListThree.add("Vivek");
        studentListThree.display();
    }
}
