// Demo of State Pattern
// This code implements the state pattern
// Taken from Head first into Design Patterns
// Interface that all state classes implement
//------------------------------------------------
package gumballwinner;

public interface State {
 
	public void insertQuarter();
	public void ejectQuarter();
	public void turnCrank();
	public void dispense();
	
	public void refill();
}
