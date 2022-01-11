# one way of implementing hash map is by using the ascii value
# an ascii value will be generated for the key of each element in a dictionary

class HashTable:
    def __init__(self):
        self.MAX = 100
        # an empty array with the max size of 100(here)
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):  # function to get the index where the value is getting stored
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, index):  # function for retrieving the value
        h = self.get_hash(index)
        return self.arr[h]

    # another function for retrieving the value
    # def get(self, index):
    #     h = self.get_hash(index)
    #     return self.arr[h]

    def __setitem__(self, key, val):  # function for adding new value
        h = self.get_hash(key)
        self.arr[h] = val

    # another function for adding new value
    # def add(self, index, val):
    #     h = self.get_hash(index)
    #     self.arr[h] = val

    def __delitem__(self, key):  # function for deleting a value
        h = self.get_hash(key)
        self.arr[h] = None


t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
print(t.arr)
print(t["march 6"])
