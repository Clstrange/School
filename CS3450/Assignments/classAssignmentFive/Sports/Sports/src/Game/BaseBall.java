package Game;

import java.io.*;

public class BaseBall extends gameTemplate {
    
    public BaseBall() {
        hasEntertainment = true;
    }

    public void initalize() {
            System.out.println("Baseball game being initialized");
	}    
    
        
    
    public void intermission() {
            System.out.println("Seventh Inning Stretch");
	}
        


    protected void addEntertainment() {
        System.out.println("Fans singing sweet carolina");
    }
 
       
       
}
