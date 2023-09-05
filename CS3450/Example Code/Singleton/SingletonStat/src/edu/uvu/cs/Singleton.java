// Singleton demo from Head first into design patterns
// Singleton class - thread safe
// L. Thackeray
//
package edu.uvu.cs;

public class Singleton {
        // create an instance: creation happens as soon as class
        //  is loaded - JVM does this
	private static Singleton uniqueInstance = new Singleton();  //init class
 
	private Singleton() {}
 
        // returns the instance - there will only be one
	public static Singleton getInstance() {
		return uniqueInstance;
	}
	
	// other useful methods here
	public String getDescription() {
		return "Hello Class, I'm a statically initialized Singleton!";
	}
}



