class DynamicArray:
    def __init__(self, capacity=10):
        self.size = 0
        self.capacity = capacity
        self.array = [None] * capacity

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[index]

    def add(self, data):
        if self.size >= self.capacity:
            self._grow()
        self.array[self.size] = data
        self.size += 1

    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size >= self.capacity:
            self._grow()
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = data
        self.size += 1

    def delete(self, data):
        for i in range(self.size):
            if self.array[i] == data:
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j + 1]
                self.array[self.size - 1] = None
                self.size -= 1
                if self.size <= self.capacity // 3:
                    self._shrink()
                break

    def search(self, data):
        for i in range(self.size):
            if self.array[i] == data:
                return i
        return -1

    def _grow(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.capacity = new_capacity
        self.array = new_array

    def _shrink(self):
        new_capacity = self.capacity // 2
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.capacity = new_capacity
        self.array = new_array

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        string = ", ".join(str(self.array[i]) for i in range(self.size))
        return f"[{string}]"


# Example usage
if __name__ == "__main__":
    dynamic_array = DynamicArray(5)

    dynamic_array.add("A")
    dynamic_array.add("B")
    dynamic_array.add("C")

    print(dynamic_array.get(0))
    # dynamic_array.insert(0, "X")
    # dynamic_array.delete("A")
    # print(dynamic_array.search("C"))

    print(dynamic_array)
    print("size:", dynamic_array.size)
    print("capacity:", dynamic_array.capacity)
    print("empty:", dynamic_array.is_empty())
