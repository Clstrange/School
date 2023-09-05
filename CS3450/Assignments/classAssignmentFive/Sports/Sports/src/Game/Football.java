package Game;

import java.io.*;

public class Football extends gameTemplate {
    
    public Football() {
        hasEntertainment = true;
    }

    public void initalize() {
            System.out.println("Football game being initialized");
	}    
    
        
    
    public void intermission() {
            System.out.println("Half-time");
	}
        


    protected void addEntertainment() {
        System.out.println("Metalica half-time show");
    }
 
       
       
}
