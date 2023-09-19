import java.util.ArrayList;

public class OrderProcessor {
    public class Order {
        private int id;
        private String name;
        private ArrayList<Item> lyst;

        public static class Item {
            private String name;
            private int quantity;
            private double price;

        }

        public Order(int id, String name) {
            this.name = name;
            this.id = id;
        }

        public void addItem(Item item) {
            this.lyst.add(item);
        }

        public double calculateTotal(ArrayList<Item> lyst) {
            double totalCost = 0;
            for (Item item: lyst
                 ) {
                totalCost += item.quantity * item.price;
            }
            return totalCost;
        }

        public ArrayList<Item>
    }

    public void display(Order order) {
        System.out.println("Name: " + order.name + "\nID: " + order.id + "\n");
        for (order.item item:
             ) {

        }
    }
}
