// Singleton demo - from Head First into Design Patterns
// Singleton class
// not thread safe
// L. Thackeray
//
package edu.uvu.cs;

public class SingletonClient {
	public static void main(String[] args) {
		Singleton singleton = Singleton.getInstance();
		System.out.println(singleton.getDescription());

		//try to create second instance (returns orig instance)
		Singleton singleton1 = Singleton.getInstance();
                
               
                
	}
}
