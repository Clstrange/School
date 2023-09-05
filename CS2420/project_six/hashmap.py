"""
Name: Cody Strange
Class: CS 2420
Project: Hashing and Caching
"""
class HashMap:
    """class for caching"""

    def __init__(self):
        """class constructor"""
        self.buckets = 7
        self.key_lyst = []
        self.value_lyst = []
        key = (0,0)
        self.hashing = ((key[0] + 4) * 3) * ((key[1] + 7) * 2)
        for i in range(10000):
            self.value_lyst.append(0)

    def get(self, key):
        """returns value of a key"""

        if key in self.key_lyst:
            return self.value_lyst[self.hashing]
        raise KeyError

    def set(self, key, value):
        """adds a key value pair to hashmap"""
        self.key_lyst.append(key)
        self.value_lyst.insert(self.hashing, value)
        if len(self.key_lyst) >= self.buckets * 0.8:
            self.buckets = self.buckets * 2 - 1


    def remove(self, key):
        """removes key value pair from hasmap"""
        temp = self.value_lyst[self.hashing]
        self.value_lyst.remove(temp)
        self.key_lyst.remove(key)

    def clear(self):
        """clears hashmap"""
        self.value_lyst.clear()
        self.key_lyst.clear()
        self.buckets = 7

    def capacity(self):
        """returns capacity of hashmap"""
        return self.buckets

    def size(self):
        """returns size of hashmap"""
        return len(self.key_lyst)

    def keys(self):
        """returns list of keys"""
        return self.key_lyst
