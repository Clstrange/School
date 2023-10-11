package com.codystrange.InnerClassesGenericsAndCollections;


import java.util.ArrayList;
import java.util.Iterator;

public class Library {
    private final ArrayList<Book> books = new ArrayList();

    public Library() {
    }

    public void addBook(Book book) {
        this.books.add(book);
    }

    public void displayBooks() {
        Iterator var1 = this.books.iterator();

        while(var1.hasNext()) {
            Book book = (Book)var1.next();
            System.out.println(book.title + ", " + book.author + " " + book.publicationYear);
        }

    }

    public static class Book {
        private final String title;
        private final String author;
        private final String publicationYear;

        public Book(String title, String author, String publicationYear) {
            this.title = title;
            this.author = author;
            this.publicationYear = publicationYear;
        }
    }
}
