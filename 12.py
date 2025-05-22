def analyze_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        total_lines = len(lines)
        total_words = 0
        total_characters = 0

        for line in lines:
            total_characters += len(line)
            words = line.split()
            total_words += len(words)

        print(f"\nAnalysis of '{filename}':")
        print(f"Total Lines: {total_lines}")
        print(f"Total Words: {total_words}")
        print(f"Total Characters: {total_characters}")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
filename = input("Enter the filename (with .txt extension): ")
analyze_file(filename)

