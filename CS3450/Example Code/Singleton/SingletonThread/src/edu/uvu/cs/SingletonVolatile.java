/*
 * Demo of "volatile" keyword
 *  Note: Broken under Java 1.4 and earlier semantics for volatile
 *  L. Thackeray
 */
package edu.uvu.cs;

/**
 * @author lthackeray
 */
public class SingletonVolatile {
        // reference, not initialization
	private volatile static SingletonVolatile uniqueInstance;
 
	private SingletonVolatile() {}  //private constructor
 
        // use "synchronized" keyword twice (double-checked locking"
	public static SingletonVolatile getInstance() {
		if (uniqueInstance == null) {
                    synchronized (SingletonVolatile.class){
                        if (uniqueInstance == null) {
                            uniqueInstance = new SingletonVolatile();
                        }
                    }  //end synchronized class
                } //end if
                    
                return uniqueInstance;
                
        } //end getInstance
	
	 
	// other useful methods here
	public String getDescription() {
		return "Hello class, I'm using the Volatile keyword!";
	}
        
} //end class


