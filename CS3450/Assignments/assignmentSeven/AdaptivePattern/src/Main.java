import java.util.ArrayList;
public class Main {
    public static void main(String[] args) throws Exception {
        Shape point = new Point();
        Shape line = new Lyne();
        Shape rectangle = new Rectangle();
        XXCircle circle = new XXCircle();
        Shape circleAd = new CircleAdapter(circle);

        ArrayList<Shape> shapeList = new ArrayList<Shape>();

        shapeList.add(point);
        shapeList.add(line);
        shapeList.add(rectangle);
        shapeList.add(circleAd);

        for (int i = 0; i < shapeList.size(); i++) {
            shapeList.get(i).display();
            System.out.println(shapeList.get(i).getLocation());
            shapeList.get(i).fill();
        }
    }
}
