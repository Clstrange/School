// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        University myUniversity = new University("Utah Valley University");

        University.Student student1 = myUniversity.new Student("Alice Wonderland");
        University.Student student2 = myUniversity.new Student ("Sonic T Hedgehog");

        student1.displayStudentInfo();
        student2.displayStudentInfo();

        MathUtil.Calculator calculator = new MathUtil.Calculator();

        int resultAdd = calculator.add(5, 3);
        int resultSubtract = calculator.subtract(10, 4);

        System.out.println("Addition Result: " + resultAdd);
        System.out.println("Subtraction Result: " + resultSubtract);

    }
}