// Demo of State Pattern
// This code implements the state pattern
// Taken from Head first into Design Patterns
// This is the interface implemented by all concreate state classes
package gumballstate;

public interface State {
 
	public void insertQuarter();
	public void ejectQuarter();
	public void turnCrank();
	public void dispense();
	
	public void refill();
}
