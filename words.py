def word_count(file_path: str):
    '''
    function counts and prints the number of words in given file
    :param file_path: path to file
    :return: none
    '''
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


def word_appear(file_path: str):
    '''
    function counts the number of times each word has appeared in a file
    :param file_path: file path
    :return: none
    '''
    try:
        with open(file_path, 'r') as file:
            content = file.read()

            # Split the content into words
            wordsList = content.split()

            wordsDict = {}
            for word in wordsList:
                if(word not in wordsDict.keys()):
                    wordsDict.update({word : 1})
                else:
                    wordsDict[word] = wordsDict[word] + 1

            print_dict(wordsDict)

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error reading the file '{file_path}'.")


def print_dict(givenDict: dict):
    '''
    function prints a dictionary
    :param givenDict: dictionary to print
    :return: none
    '''
    for key, value in givenDict.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    path = r"C:\Users\magshimim\Documents\Omega Projects\Python\lesson2\one.txt"
    word_count(path)
    word_appear(path)