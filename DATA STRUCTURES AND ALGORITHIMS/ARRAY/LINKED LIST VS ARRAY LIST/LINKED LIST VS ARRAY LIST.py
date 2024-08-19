from collections import deque
import time


def main():
    linked_list = deque()
    array_list = []

    # Populating the lists
    for i in range(1000000):
        linked_list.append(i)
        array_list.append(i)

    # ****************LinkedList****************
    start_time = time.time_ns()

    # Access the first element
    _ = linked_list[0]
    # _ = linked_list[500000]
    # _ = linked_list[999999]
    # linked_list.popleft()  # Remove the first element
    # del linked_list[500000]  # This will be slow as it requires shifting elements
    # linked_list.pop()  # Remove the last element

    end_time = time.time_ns()
    elapsed_time = end_time - start_time

    print(f"LinkedList:\t{elapsed_time} ns")

    # ****************ArrayList****************
    start_time = time.time_ns()

    # Access the first element
    _ = array_list[0]
    # _ = array_list[500000]
    # _ = array_list[999999]
    # del array_list[0]  # Remove the first element
    # del array_list[500000]  # Remove the middle element
    # del array_list[-1]  # Remove the last element

    end_time = time.time_ns()
    elapsed_time = end_time - start_time

    print(f"ArrayList:\t{elapsed_time} ns")


if __name__ == "__main__":
    main()
Explanation
