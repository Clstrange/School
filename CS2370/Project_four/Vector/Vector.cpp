// Vector.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include "Vector.h"
#include <algorithm>
#include <iterator>
#include <stdexcept>
#include <cstddef>
using namespace std;

// Private
void Vector::grow() {
    capacity = capacity * 1.6;
    int* tempPointer = new int[capacity];  
    for (int i = 0; i < n_elems; i++) {
        tempPointer[i] = data_ptr[i];
    }
    delete[] data_ptr;
    data_ptr = tempPointer;
    tempPointer = nullptr;
}

// Object Mtg
Vector::Vector() {
    data_ptr = new int[CHUNK];
    capacity = CHUNK;
    n_elems = 0;
}

Vector::Vector(const Vector& v) {
    capacity = v.capacity;
    n_elems = v.n_elems;
    data_ptr = new int[capacity];
    for (int i = 0; i < n_elems; i++) {
        data_ptr[i] = v.data_ptr[i];
    }
}

Vector& Vector::operator=(const Vector& v) {
    this->capacity = v.capacity;
    this->n_elems = v.n_elems;
    delete[] this->data_ptr;
    this->data_ptr = new int[capacity];
    for (int i = 0; i < this->n_elems; i++) {
        this->data_ptr[i] = v.data_ptr[i];
    }
    return *this;
}

Vector::~Vector() {

    //loop through data_ptr and delete each item

}


// Accessors
int Vector::front() const {
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

int Vector::back() const {
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

int Vector::at(size_t pos) const {
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

size_t Vector::size() const {
    return this->n_elems;
}

bool Vector::empty() const {
    return n_elems == 0;
}

// Mutators
int& Vector::operator[](size_t pos) {
    return data_ptr[pos];
}

void Vector::push_back(int item) {
    n_elems += 1;
    if (n_elems == capacity) {
        this->grow();
    }
    data_ptr[n_elems - 1] = item;

}

void Vector::pop_back() {

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

void Vector::erase(size_t pos){
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

void Vector::insert(size_t pos, int item) {
    n_elems += 1;
    if (n_elems > capacity) {
        this->grow();
    }

    for (int i = capacity - 1; i > pos; i--) {
        data_ptr[i] = data_ptr[i - 1];
    }
    data_ptr[pos] = item;

}

void Vector::clear() {
    n_elems = 0;
}

// Iterators
int* Vector::begin() {
    if (n_elems == 0) {
        return nullptr;
    }
    return &data_ptr[0];
}

int* Vector::end() {
    if (n_elems == 0) {
        return nullptr;
    }
    return &data_ptr[n_elems];
}

// Comparators
bool Vector::operator==(const Vector& v) const {
    return true;
}

bool Vector::operator!=(const Vector& v) const {
    return true;
}
