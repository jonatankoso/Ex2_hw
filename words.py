def word_count(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

            # Split the content into words
            words = content.split()

            # Count the number of words
            word_count = len(words)
            print(f"The file '{file_path}' contains {word_count} words.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error reading the file '{file_path}'.")


if __name__ == "__main__":
    word_count(r"C:\Users\magshimim\Documents\Omega Projects\Python\lesson2\one.txt")