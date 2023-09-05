// Singleton demo from Head first into design patterns
// Singleton class - thread safe
// L. Thackeray
//
package edu.uvu.cs;

public class SingletonClient {
	public static void main(String[] args) {
		int var1 = 45;  // test code to show static initialization (evaluate uniqueInstance at this point)
		Singleton singleton = Singleton.getInstance();
		System.out.println(singleton.getDescription());
	}
}
