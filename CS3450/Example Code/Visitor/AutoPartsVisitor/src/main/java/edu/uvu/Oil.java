package edu.uvu;

public class Oil implements AutoPart {
	@Override
	public void accept(AutoPartVisitor visitor) {
		visitor.visit(this);
	}
}
