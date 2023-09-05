public abstract class Shape {
    public void setLocation() {
        System.out.println("Set the shape's location");
    }

    public String getLocation() {
        return ("'Shape's Location'");
    }

    public void setColor() {
        System.out.print("Set the shape's color");
    }

    abstract void display();
    abstract void fill();
    abstract void undisplay();
}
