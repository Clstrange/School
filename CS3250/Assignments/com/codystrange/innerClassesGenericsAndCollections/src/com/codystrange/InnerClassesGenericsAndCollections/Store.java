package com.codystrange.InnerClassesGenericsAndCollections;

import java.util.ArrayList;
import java.util.Arrays;

public class Store {
    private final Map catalog;

    public Store() {
        catalog = new Map();
    }

    public static class Map {
        private String id;
        private ArrayList<String> data;
        private final ArrayList<Map> maps = new ArrayList<>();

        public Map() {

        }
        public Map(String id, ArrayList<String> data) {
            this.id = id;
            this.data = data;
        }

        public void add(Product product) {
            maps.add(new Map(product.productID,new ArrayList<String>(Arrays.asList(product.productName,product.price))));
        }

        public ArrayList<String> get(String id) {
            for (Map map:maps
                 ) {
                if (map.id.equals(id)) {
                    return map.data;
                }


            }
            System.out.println("No ID found");
            return new ArrayList<String>();
        }
    }

    public static class Product {
        private String productID;
        private String productName;
        private String price;

        public Product(String productID,String productName, String price) {
            this.price = price;
            this.productID = productID;
            this.productName = productName;
        }
    }

    public void createProduct(String productID,String productName, String price) {
        catalog.add(new Product(productID, productName, price));
    }

    public void findProductWithHighestPrice() {

    }
}
