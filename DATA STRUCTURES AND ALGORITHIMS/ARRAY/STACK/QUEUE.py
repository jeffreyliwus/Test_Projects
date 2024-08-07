from collections import deque


# Queue class definition
class Queue:
    def __init__(self):
        self.queue = deque()

    def offer(self, item):
        self.queue.append(item)

    def poll(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def contains(self, item):
        return item in self.queue

    def __str__(self):
        return str(list(self.queue))


# Main function equivalent
if __name__ == "__main__":
    queue = Queue()

    queue.offer("Karen")
    queue.offer("Chad")
    queue.offer("Steve")
    queue.offer("Harold")

    # Uncomment the following lines to test the queue functionality
    # print(queue.is_empty())       # Check if the queue is empty
    # print(queue.size())           # Get the size of the queue
    # print(queue.contains("Harold")) # Check if the queue contains "Harold"

    # print(queue.peek())           # Peek at the front of the queue
    # queue.poll()                  # Dequeue an item
    # queue.poll()                  # Dequeue another item
    # queue.poll()                  # Dequeue another item
    # queue.poll()                  # Dequeue another item

    print(queue)  # Print the current state of the queue
