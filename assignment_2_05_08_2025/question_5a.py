def lensort(lst):
    return sorted(lst, key=len)

if __name__ == "__main__":
    example_list = ["apple", "banana", "kiwi", "cherry", "blueberry"]
    sorted_list = lensort(example_list)
    print(sorted_list)