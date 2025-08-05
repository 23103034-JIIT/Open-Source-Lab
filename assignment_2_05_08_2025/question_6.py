def readFile(filename):
    with open(filename, 'r') as file:
        return file.readlines()

if __name__ == "__main__":
    filename = 'data.txt'
    try:
        lines = readFile(filename)
        for line in lines:
            print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
