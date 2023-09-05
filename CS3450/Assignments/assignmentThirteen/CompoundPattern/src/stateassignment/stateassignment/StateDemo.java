// represents a fan with settings speed settings (states) of
// low, medium, high, and off.
// by pulling the fan chain you can cycle through these settings


package stateassignment;

import java.io.*;

public class StateDemo {
    public static void main(String[] args) {

        Fan fan = new Fan();
        Remote remote = new Remote();

        remote.press(new Low(fan));
        remote.press(new High(fan));
        remote.press(new Off(fan));
        remote.press(new High(fan));
        remote.press(new Medium(fan));
        remote.press(new Off(fan));
        
        }

}