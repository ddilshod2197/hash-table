class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return

    def display(self):
        for index, bucket in enumerate(self.table):
            print(f"Bucket {index}: {bucket}")


# Test
hash_table = HashTable(10)
hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")
hash_table.display()
print(hash_table.get("key1"))
hash_table.delete("key1")
hash_table.display()
