/**
 * auto parts inventory
 * using Visitor pattern
 */
package edu.uvu;

public class VisitorDemo {

	public static void main(String[] args) {
		PartsOrder order = new PartsOrder();
		order.addPart(new Wheel());
		order.addPart(new Fender());
		order.addPart(new Oil());

		//visitor
		order.accept(new AutoPartsShippingVisitor());
	//	order.accept(new AutoPartsDisplayVisitor());
	}
}
