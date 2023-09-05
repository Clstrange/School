

#include <iostream>
#include <string>
#include <assert.h>
#include <bitset>
using namespace std;


class Bits {
    using IType = unsigned long long; // We only have to change the integer type here, if desired
    enum { NBITS = sizeof(IType) * 8 };
    IType bits = 0;
public:
    Bits() = default;
    Bits(IType n) {
        bits = n;
    }
    static int size() {
        return NBITS;
    }
    bool at(int pos) const {  // Returns (tests) the bit at bit-position pos
        assert(0 <= pos && pos < NBITS);
        return bits & (IType(1) << pos);
    }
    void set(int pos) {  // Sets the bit at position pos
        assert(0 <= pos && pos < NBITS);
        bits |= (IType(1) << (pos - 1));
    };
    void set() {
        for (int i = 0; i < NBITS; i++) {  // Sets all bits
            this->set(i);
        }
    };
    void reset(int pos) {  // Resets (makes zero) the bit at position pos
        assert(0 <= pos && pos < NBITS);
        bits &= ~(IType(1) << (pos - 1));
        cout << bits;

    };
    void reset() {
        for (int i = 0; i < NBITS; i++) {
            this->reset(i);
        }
    };
    void assign(int pos, bool val) { // Sets or resets the bit at position pos depending on val
        assert(0 <= pos && pos < NBITS);
        if (val == true) {
            this->set(pos);
        }
        else {
            this->reset(pos);
        }

    }; 
    void assign(IType n) {  // Replaces the underlying integer with n
        bits = n;
    };     
    void toggle(int pos) {  // Flips the bit at position pos
        bits ^= (IType(1) << (pos - 1));
    };     
    void toggle() {  // Flips all bits
        for (int i = 0; i < NBITS; i++) {
            this->toggle(i);
        }
    };            
    void shift(int n) {// If n > 0, shifts bits right n places; if n < 0, shifts left
        if (n > 0) {
            bits = bits >> n;
        }
        else if (n < 0) {
            bits = bits << abs(n);
        }
    };
    void rotate(int n) {  // If n > 0, rotates right n places; if n < 0, rotates left
        
        if (n < 0) {
            bits = (bits << abs(n)) | (n >> (IType(1) - abs(n)));
        }
        else if (n > 0) {
            bits = (bits >> n) | (n >> (IType(0) - abs(n)));
        }
        cout << bits;
    };       
    int ones() const {
        int x = 0;
        for (int i = 0; i < NBITS; i++) {  // Returns how many bits are set in the underlying integer
            
            if (this->at(i) == 1) {
                
                x += 1;
            }
        }
        return x;
    };         
    int zeroes() const {      // Returns how many bits are reset in the underlying integer
        return NBITS - ones();
    }
    IType to_int() const {
        return bits;
    }
    friend bool operator==(const Bits& b1, const Bits& b2) {
        return b1.bits == b2.bits;
    }
    friend bool operator!=(const Bits& b1, const Bits& b2) {
        return b1.bits != b2.bits;
    }
    friend std::ostream& operator<<(std::ostream& os, const Bits& b) {
        return os << std::bitset<NBITS>(b.bits);    // Be sure to #include <bitset>
    }
};

