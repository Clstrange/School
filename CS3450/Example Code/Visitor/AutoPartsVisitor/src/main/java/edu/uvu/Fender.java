package edu.uvu;

public class Fender implements AutoPart {
	@Override
	public void accept(AutoPartVisitor visitor) {
		visitor.visit(this);
	}
}
