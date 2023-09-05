public class Point extends Shape {
    @Override
    void display() {
        System.out.println("Displaying a Point");
    }

    @Override
    void fill() {
        System.out.println("Filling a Point");
    }

    @Override
    void undisplay() {
        System.out.println("Undisplaying a Point");
    }
    
}
