use std::f64::consts::PI;

// Exercise One
fn compose(x: i32, f: fn(i32)->i32, g: fn(i32)->i32 ) ->i32{
    return f(g(x));
}

// Exercise Two
use Shape::Circle;
use Shape::Rectangle;

enum Shape {
    Circle(f64),
    Rectangle(f64,f64),
}

impl Shape {
    fn area(&self) -> f64 {
        match *self {
            Shape::Circle(radius) => PI * radius.powi(2),
            Shape::Rectangle(length, width) => length * width,
        }
    }
}

// Exercise Three
fn f2n<T>(f: fn(T)->T, n: u32, x: T) -> T {
    if n < 1 {
        return x;
    }
    return f2n(f,n-1,f(x));

}

/* Output:
256.0
"foo+++"
*/