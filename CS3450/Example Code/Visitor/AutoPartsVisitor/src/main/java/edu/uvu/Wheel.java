package edu.uvu;

public class Wheel implements AutoPart {
	@Override
	public void accept(AutoPartVisitor visitor) {
		visitor.visit(this);
	}
}
