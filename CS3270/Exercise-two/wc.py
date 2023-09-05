"""
    Cody Strange
    9/7/2022
    CS3270-001
    Programming Exercise 2

    Summary:
        This program should read in a text file and 
        print out to another text file the amount of each words that 
        appear in the text. The printed text file should be sorted in 
        descending order by the quanity of words in the text.

    Version 1 --- 9/7/2022
        pre-session summary: The program looks simple, my plan is to determine what qualifies
        as a word then either put that word in a dictionary as a key and one as its value, or increment
        its value if it is already in the dictionary. I will then sort the dictionary by value and then print out
        each key value pair formatted properly.

        post-session summary: Design and implemenatation of code worked nearly flawlessly first time around. Note
        worthy changes consisted of.
            - I had to sort the keys in the dictionary by value and store those keys in a list, I then printed
            out each string in that list and its corresponding value in the actual dictionary
            - Had to use the .format when printing to get the right-aligned style that the project
            required.
        Overall I was very happy with how the project turned out, I was able to accurately work out the logic in my
        design and it converted over to code very smoothly and in less than 30 lines of code.
    
    Bugs:
        - none found

    Required features:
        - none remaining

    Reccomended features
        - remove first for-loop and replace with raw_text.read()

"""
import string
def main():
    with open("Strings.txt", 'r') as raw_text:
        word_dictionary = {} # storing each word and its word count as key/value pairs
        word = "" # used to create words from individual characters in the text
        for text in raw_text: # should've just used raw_text.read()
            for character in text:
                character = character.lower() # make it so uppercase and lowercase words count as the same word
                if character.isalpha() or character == "'": # only acceptable characters in what is being defined as a word
                    word += character
                elif character in string.punctuation or character.isspace(): # finding the end of a word
                    if len(word) > 0: # ignore random whitespace and punctuation
                        if word in word_dictionary.keys():
                            word_dictionary[word] += 1
                        else:
                            word_dictionary[word] = 1
                        word=""
        word_hierarchy = sorted(word_dictionary, key=lambda k: word_dictionary[k], reverse=True) # create a list of the keys that is sorted by their value
        for key in word_hierarchy:
            print('{:>20}: {:>5}'.format(key, str(word_dictionary[key]))) # formatted by greatest value to least value
if __name__ == "__main__":
    main()