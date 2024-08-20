def linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1


def main():
    # linear search = Iterate through a collection one element at a time

    array = [9, 1, 8, 2, 7, 3, 6, 4, 5]

    index = linear_search(array, 5)

    if index != -1:
        print(f"Element found at index: {index}")
    else:
        print("Element not found")


if __name__ == "__main__":
    main()
