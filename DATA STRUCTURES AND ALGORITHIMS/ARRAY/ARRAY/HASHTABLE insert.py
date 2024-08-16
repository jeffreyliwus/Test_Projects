"""HASHTABLE class implements a hash table using separate chaining with linked list to resolve collisions. 
This particular implementation is designed to store key-value pairs, where keys are strings, and values are
numbers"""


class HashTable:
    def __init__(self, capacity, hash_function_type):
        self.bucket_array = [None] * capacity
        ...

    def put(self, key, value):
        # Inserts or updates a key-value pair in the hash table.
        ...

    def get(self, key):
        # retrives the value associated with a given key
        ...

    def remove(self, key):
        # removes a key-value pair from hash table
        ...
