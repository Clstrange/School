// Singleton demo (head first design patterns)
// Singleton class - Thread safe
// driver class
// L. Thackeray
//
package edu.uvu.cs;

public class SingletonClient {
	public static void main(String[] args) {
		Singleton singleton = Singleton.getInstance();
		System.out.println(singleton.getDescription());
                
                                
		SingletonVolatile singletonV = SingletonVolatile.getInstance();
		System.out.println(singletonV.getDescription());
	}
}
