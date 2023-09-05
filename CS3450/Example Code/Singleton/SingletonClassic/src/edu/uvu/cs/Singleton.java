// Singleton demo - from Head First into Design Patterns
// Singleton class
// not thread safe
// L. Thackeray
//
package edu.uvu.cs;
/**
 * 
 * @author lthackeray
 * Singleton class
 */
public class Singleton {
        /**
         * static - belongs to the class, not the instance object
         * private - accessible only by instance methods
         */
        private static Singleton uniqueInstance;
       
        /**
         * private constructor - prevents outside instantiation
         */
	private Singleton() {}
 
        /**
         * Lazy instantiation - public and static ensures it can be accessed anywhere/anytime
         * @param - none
         * @return - instance (reference) of singleton class
         */
	public static Singleton getInstance() {
		if (uniqueInstance == null) {
			uniqueInstance = new Singleton();
		}
		return uniqueInstance;
	}
       
	public String getDescription() {
		return "Hello class, I'm a classic Singleton!";
	}
}




