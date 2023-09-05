// Singleton demo (head first design patterns)
// Singleton class - Thread safe
// L. Thackeray
//
package edu.uvu.cs;

public class Singleton {
        // reference, not initialization
	private static Singleton uniqueInstance;
 
	private Singleton() {}
 
        // use "synchronized" keyword
        // Lazy creation
	public static synchronized Singleton getInstance() {
		if (uniqueInstance == null) {
			uniqueInstance = new Singleton();
		}
		return uniqueInstance;
	}
 
	// other useful methods here
	public String getDescription() {
		return "Hello class, I'm a thread safe Singleton!";
	}
}
