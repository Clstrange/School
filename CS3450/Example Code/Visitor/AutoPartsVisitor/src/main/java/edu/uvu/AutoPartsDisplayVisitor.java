/**
 * Concrete Visitor
 */
package edu.uvu;

public class AutoPartsDisplayVisitor implements AutoPartVisitor {

	@Override
	public void visit(Wheel wheel) {
		System.out.println("We have a wheel.");
	}

	@Override
	public void visit(Fender fender) {
		System.out.println("We have a fender.");

	}

	@Override
	public void visit(Oil oil) {
		System.out.println("We have oil.");

	}

	@Override
	public void visit(PartsOrder partsOrder) {
		System.out.println("We have an order.");

	}

}
