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

	public double calculateShipping() {
		double shippingCost = 0;
		for (AutoPart autoPart : parts) {
			shippingCost += autoPart.calculateShipping();
		}
		return shippingCost;
	}
	
}
