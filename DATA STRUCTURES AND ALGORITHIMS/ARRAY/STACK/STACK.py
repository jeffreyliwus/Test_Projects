# *******************************************************

# stack = LIFO data structure. Last-In First-Out
#               stores objects into a sort of "vertical tower"
#               append() to add objects to the top
#               pop() to remove objects from the top

# uses of stacks?
# 1. undo/redo features in text editors
# 2. moving back/forward through browser history
# 3. backtracking algorithms (maze, file directories)
# 4. calling functions (call stack)

# *******************************************************


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def search(self, item):
        if item in self.stack:
            return self.stack.index(item) + 1
        return -1

    def __str__(self):
        return str(self.stack)


def main():
    stack = Stack()

    # Uncomment the following line to check if the stack is empty
    # print(stack.is_empty())

    stack.push("Minecraft")

    stack.push("Skyrim")
    stack.push("DOOM")
    stack.push("Borderlands")
    stack.push("FFVII")

    # Uncomment the following lines to perform pop, peek, and search operations
    # my_fav_game = stack.pop()
    # print(stack.peek())
    # print(stack.search("Fallout76"))

    my_fav_game = stack.pop()  # This line now correctly calls the pop method
    print(my_fav_game)  # This will print the popped item
    print(stack.peek())  # This will print the current top item
    print(stack.search("DOOM"))  # This will search for "DOOM" in the stack
    print(stack)  # This will print the current state of the stack

    print(
        stack.is_empty()
    )  # This will check if stack is empty before and after performing some operations.


if __name__ == "__main__":
    main()
