/**
 * Driver (test) program
 * for State assignment
 */
package bikegearing;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class StateDemo {
    public static void main(String[] args) {
        
        FirstGear first = new FirstGear();
        SecondGear second = new SecondGear();
        ThirdGear third = new ThirdGear();
          
        String input;
        
         System.out.print("** start autoshift sequence **\n"); 
    
        do {
            first.gearUp();
            second.gearUp();
            third.gearUp();
            third.gearDown();
            second.gearDown();
            first.gearDown();
            System.out.print("Another autoshift sequece? (Y/N): ");  
            input = getLine();
        }while (input.equalsIgnoreCase("Y"));
        
        System.out.print("** autoshift sequence complete **\n");  
    }
    
       

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