/**
 * Element Interface
 * original solution interface now with
 * Visitor accept method (this is the hook the visitor uses)
 */

package edu.uvu;

public interface AutoPart {
	public void accept(AutoPartVisitor visitor);
}
