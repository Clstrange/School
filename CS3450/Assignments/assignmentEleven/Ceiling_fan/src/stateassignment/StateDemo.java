// represents a fan with settings speed settings (states) of
// low, medium, high, and off.
// by pulling the fan chain you can cycle through these settings


package stateassignment;

import java.io.*;

public class StateDemo {
    public static void main(String[] args) {
        final int MAX_CNT = 8;  //number of cycles for test
        //instantiate fan class
        Fan chain = new Fan();
        for (int testCnt = 1; testCnt <= MAX_CNT; testCnt++)
            
        {
            System.out.print("Press ENTER");
            getLine();
            chain.pull();
        }
        
        }
    
    // output status on fan states
    static String getLine() {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line = null;
        try {
            line = in.readLine();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        return line;
    }
}