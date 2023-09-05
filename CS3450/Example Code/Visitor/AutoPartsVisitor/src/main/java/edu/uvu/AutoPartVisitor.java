/**
 * Main Visitor Interface
 */

package edu.uvu;

public interface AutoPartVisitor {

	// these methods will "visit" original program
	// concrete classes
	void visit(Wheel wheel);
	void visit(Fender fender);
	void visit(Oil oil);
	void visit(PartsOrder partsOrder);
}
