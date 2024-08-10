from collections import deque


def main():
    # *****************************************************

    # LinkedList =  Nodes are in 2 parts (data + address)
    #               Nodes are in non-consecutive memory locations
    #               Elements are linked using pointers

    #    advantages?
    #    1. Dynamic Data Structure (allocates needed memory while running)
    #    2. Insertion and Deletion of Nodes is easy. O(1)
    #    3. No/Low memory waste

    #    disadvantages?
    #    1. Greater memory usage (additional pointer)
    #    2. No random access of elements (no index [i])
    #    3. Accessing/searching elements is more time consuming. O(n)

    #    uses?
    #    1. implement Stacks/Queues
    #    2. GPS navigation
    #    3. music playlist
    #

    # *****************************************************

    linked_list = deque()

    # Uncomment the following lines to use the deque as a stack
    """
    linked_list.appendleft("A")
    linked_list.appendleft("B")
    linked_list.appendleft("C")
    linked_list.appendleft("D")
    linked_list.appendleft("F")
    linked_list.popleft()
    """

    # LinkedList as a Queue
    linked_list.append("A")
    linked_list.append("B")
    linked_list.append("C")
    linked_list.append("D")
    linked_list.append("F")
    # linked_list.popleft()

    # linked_list.insert(4, "E")  # Insert "E" at position 4 (zero-indexed)
    # linked_list.remove("E")  # Remove the first occurrence of "E"
    # print(linked_list.index("F"))  # Find the index of "F"

    # print(linked_list[0])  # Peek at the first element
    # print(linked_list[-1])  # Peek at the last element
    # linked_list.appendleft("0")  # Add "0" at the beginning
    # linked_list.append("G")  # Add "G" at the end
    # first = linked_list.popleft()  # Remove and return the first element
    # last = linked_list.pop()  # Remove and return the last element

    print(list(linked_list))


if __name__ == "__main__":
    main()
