def split_list(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

if __name__ == "__main__":
    integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(split_list(integers, 3))