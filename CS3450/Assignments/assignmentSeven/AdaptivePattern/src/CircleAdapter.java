public class CircleAdapter extends Shape {
    XXCircle circle = null;

    public CircleAdapter(XXCircle circle) {
        this.circle = circle;
    }

    @Override
    public void setLocation() {
        this.circle.setLocation();
    }

    @Override
    public String getLocation() {
        return this.circle.getLocation();
    }  

    @Override
    void display() {
        this.circle.displayIt();
    }

    @Override
    void fill() {
       this.circle.fillIt();
    }

    @Override
    void undisplay() {
       this.circle.undisplayIt();
    }
    
}
