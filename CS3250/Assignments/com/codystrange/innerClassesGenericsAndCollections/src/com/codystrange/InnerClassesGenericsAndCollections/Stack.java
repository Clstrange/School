package com.codystrange.InnerClassesGenericsAndCollections;


import java.util.ArrayList;

public class Stack<T> {
    private final ArrayList<T> stack = new ArrayList();

    public Stack() {
    }

    public void push(T item) {
        this.stack.add(item);
    }

    public T pop() {
        T item = this.stack.get(this.stack.size() - 1);
        this.stack.remove(item);
        return item;
    }

    public boolean isEmpty() {
        return this.stack.size() == 0;
    }

    public T peek() {
        return this.stack.get(this.stack.size() - 1);
    }
}

