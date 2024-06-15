import os
from collections import defaultdict

def count_words(text):
    """
    This function takes a string and returns the number of words in the string.
    """
    words = text.split()
    return len(words)

def count_characters(text):
    """
    This function takes a string and returns a dictionary with the counts of each character.
    The characters are converted to lowercase to avoid duplicates.
    """
    char_count = defaultdict(int)
    for char in text.lower():
        if char.isalpha():  # Only count alphabetic characters
            char_count[char] += 1
    return dict(char_count)

def generate_report(path, word_count, char_count):
    """
    This function generates and prints a report of the word and character counts.
    """
    # Sort characters by frequency
    sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print()
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

def main():
    # Print the current working directory
    print(f"Current working directory: {os.getcwd()}")

    # Define the path to the book file
    path_to_file = 'github.com/JakeupSmith/bookbot/books/frankenstein.txt'
    
    # Open and read the file contents
    with open(path_to_file, 'r') as f:
        file_contents = f.read()
    
    # Count the number of words in the file contents
    word_count = count_words(file_contents)
    
    # Count the characters in the file contents
    char_count = count_characters(file_contents)
    
    # Generate and print the report
    generate_report(path_to_file, word_count, char_count)

# Call the main function
if __name__ == "__main__":
    main()
