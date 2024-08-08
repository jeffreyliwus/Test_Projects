import queue

# Main function equivalent
if __name__ == "__main__":
    # Priority Queue = A FIFO data structure that serves elements
    #                 with the highest priorities first
    #                 before elements with lower priority

    # Strings in default order
    pq = queue.PriorityQueue()

    # Strings in reverse order (to mimic Java's reverse order PriorityQueue)
    # Use negative ordinals for reverse priority in Python
    # pq = queue.PriorityQueue()
    # elements = [("B", -ord('B')), ("C", -ord('C')), ("A", -ord('A')), ("F", -ord('F')), ("D", -ord('D'))]
    # for element in elements:
    #     pq.put(element)

    # If reverse order is not needed, just add normally
    pq.put("B")
    pq.put("C")
    pq.put("A")
    pq.put("F")
    pq.put("D")

    while not pq.empty():
        print(pq.get())
