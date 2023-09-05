/**
 * Object Structure
 * called by client
 */
package edu.uvu;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class PartsOrder implements AutoPart {
	
	private List<AutoPart> parts = new ArrayList<>();
	
	public PartsOrder() {
		
	}
	
	public void addPart(AutoPart autoPart) {
		parts.add(autoPart);
	}
	
	public List<AutoPart> getParts() {
		return Collections.unmodifiableList(parts);
	}

	/**
	 * uses composition
	 * @param concrete Visitor objects
	 */
	@Override
	public void accept(AutoPartVisitor visitor) {
		for (AutoPart autoPart : parts) {
			autoPart.accept(visitor);
		}
		visitor.visit(this);
	}
}
