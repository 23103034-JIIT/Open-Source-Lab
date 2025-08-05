def reverse_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        print(line.strip()[::-1])

if __name__ == "__main__":
    file_path = 'data.txt'  # Replace with your file path
    reverse_line(file_path)