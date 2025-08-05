def reverse_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
    
    with open(output_file, 'w') as outfile:
        for line in reversed(lines):
            outfile.write(line)

if __name__ == "__main__":
    input_file = 'data.txt'
    output_file = 'output.txt'
    reverse_file(input_file, output_file)
    print(f"Reversed content written to {output_file}")