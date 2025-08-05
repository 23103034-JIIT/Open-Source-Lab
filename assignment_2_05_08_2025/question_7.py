def count_file_contents(file_path):
    with open(file_path, 'r') as file:
        data = file.read();
        num_characters = len(data)
        num_words = len(data.split())
        num_lines = len(data.splitlines())
    return num_characters, num_words, num_lines

if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")
    try:
        characters, words, lines = count_file_contents(file_path)
        print(f"Number of characters: {characters}")
        print(f"Number of words: {words}")
        print(f"Number of lines: {lines}")
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")