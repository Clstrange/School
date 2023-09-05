package edu.uvu;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        List<GeometryDraw> shapes = new ArrayList<>();
       // ArrayList shapes = new ArrayList();
        shapes.add(new GeoSquare());
        shapes.add(new GeoRectangle());
        shapes.add(new GeoCircle());

       for(GeometryDraw shape : shapes){
           shape.create();
       }

    }
}
