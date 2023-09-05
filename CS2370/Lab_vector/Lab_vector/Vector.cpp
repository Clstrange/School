// Vector.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include "Vector.h"
#include <algorithm>
#include <iterator>
#include <stdexcept>
#include <cstddef>
using namespace std;
template<typename T>
// Private
void Vector<T>::grow() {
    capacity = capacity * 1.6;
    int* tempPointer = new int[capacity];  
    for (int i = 0; i < n_elems; i++) {
        tempPointer[i] = data_ptr[i];
    }
    delete[] data_ptr;
    data_ptr = tempPointer;
    tempPointer = nullptr;
}
template<typename T>
// Object Mtg
Vector<T>::Vector() {
    data_ptr = new int[CHUNK];
    capacity = CHUNK;
    n_elems = 0;
}
template<typename T>
Vector<T>::Vector(const Vector& v) {
    capacity = v.capacity;
    n_elems = v.n_elems;
    data_ptr = new int[capacity];
    for (int i = 0; i < n_elems; i++) {
        data_ptr[i] = v.data_ptr[i];
    }
}
template<typename T>
Vector<T>& Vector<T>::operator=(const Vector<T> &v) {
    this->capacity = v.capacity;
    this->n_elems = v.n_elems;
    delete[] this->data_ptr;
    this->data_ptr = new int[capacity];
    for (int i = 0; i < this->n_elems; i++) {
        this->data_ptr[i] = v.data_ptr[i];
    }
    return *this;
}
template<typename T>
Vector<T>::~Vector() {

    //loop through data_ptr and delete each item

}


// Accessors
template<typename T>
int Vector<T>::front() const {
    try {
        if (n_elems == 0) {
            throw range_error("No elements in vector to pop");
        }
    }
    catch (range_error e) {
        throw range_error("No elements in vector to pop");

    }
    return data_ptr[0];
}
template<typename T>
int Vector<T>::back() const {
    try {
        if (n_elems == 0) {
            throw range_error("No elements in vector to pop");
        }
    }
    catch (range_error e) {
        throw range_error("No elements in vector to pop");

    }
    return data_ptr[n_elems - 1];

}
template<typename T>
int Vector<T>::at(size_t pos) const {
    try {
        if (pos >= this->n_elems) {
            throw range_error("range_error");
        }
        
    }
    catch (range_error e) {
        throw range_error("range_error");
        
    }
    return this->data_ptr[pos];
}

template<typename T>
size_t Vector<T>::size() const {
    return this->n_elems;
}
template<typename T>
bool Vector<T>::empty() const {
    return n_elems == 0;
}

// Mutators
template<typename T>
int& Vector<T>::operator[](size_t pos) {
    return data_ptr[pos];
}

template<typename T>
void Vector<T>::push_back(int item) {
    n_elems += 1;
    if (n_elems == capacity) {
        this->grow();
    }
    data_ptr[n_elems - 1] = item;

}

template<typename T>
void Vector<T>::pop_back() {

    try {
        if (n_elems == 0) {
            throw range_error("No elements in vector to pop");
        }
    }
    catch(range_error e){
        throw range_error("No elements in vector to pop");

    }

    this->n_elems -= 1;

}

template<typename T>
void Vector<T>::erase(size_t pos){
    try {
        if (pos >= n_elems) {
            throw range_error("No elements in vector to pop");
        }
    }
    catch (range_error e) {
        throw range_error("No elements in vector to pop");

    }

    for (int i = pos + 1; i < capacity - 1; i++) {
        data_ptr[i - 1] = data_ptr[i];
    }
    n_elems -= 1;
}

template<typename T>
void Vector<T>::insert(size_t pos, int item) {
    n_elems += 1;
    if (n_elems > capacity) {
        this->grow();
    }

    for (int i = capacity - 1; i > pos; i--) {
        data_ptr[i] = data_ptr[i - 1];
    }
    data_ptr[pos] = item;

}

template<typename T>
void Vector<T>::clear() {
    n_elems = 0;
}

// Iterators
template<typename T>
int* Vector<T> ::begin() {
    if (n_elems == 0) {
        return nullptr;
    }
    return &data_ptr[0];
}

template<typename T>
int* Vector<T>::end() {
    if (n_elems == 0) {
        return nullptr;
    }
    return &data_ptr[n_elems];
}

// Comparators
template<typename T>
bool Vector<T>::operator==(const Vector& v) const {
    return true;
}

template<typename T>
bool Vector<T>::operator!=(const Vector& v) const {
    return true;
}
