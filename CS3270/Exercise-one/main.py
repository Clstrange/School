"""
    Cody Strange
    4/8/2022
    CS3270-001
    Programming Exercise 1

    Summary:
        This program should read in a text file that the user inputs and
        print out a list of statistcs for the file. These statistcs should
        consist of the following list
            - Characters
            - Uppercase
            - Lowercase
            - Digits
            - White space
            - Vowels
            - Consonants
            - Sentences
            - Average words per sentence

    Version 1 --- 8/26/2022
        pre-session summary: Having finished designing the program in lucid chart and
        commenting the functions required, I am ready to write up the first 
        version of the program

        post-session summary: had to adjust the count_chars function because I didn't realize
        white-space were supposed to be counted as characters. Also messed up
        on the count_consonants function.
    
    Bugs:

    Required features:

"""


def count_chars(text):
    """Count the number of characters in the text(counting white-space)"""
    char_count = 0
    for char in text:
        char_count += 1
    return char_count


def count_upper_chars(text):
    """Count the number of upper case characters in the text"""
    upper_count = 0
    for char in text:
        if char.isupper():
            upper_count += 1
    return upper_count

def count_lower_chars(text):
    """Count the number of lower case characters in the text"""
    lower_count = 0
    for char in text:
        if char.islower():
            lower_count += 1
    return lower_count

def count_digits(text):
    """Count the number of digits in the text"""
    digit_count = 0
    for char in text:
        if char.isdigit():
            digit_count += 1
    return digit_count

def count_white_space(text):
    """Count the number of white space in the text"""
    space_count = 0
    for char in text:
        if char.isspace():
            space_count += 1
    return space_count

def count_vowels(text):
    """Count the number of each vowel (a, e, i, o, u) in the text"""
    vowels_count = {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0}
    for char in text:
        if char.lower() in vowels_count:
            vowels_count[char.lower()] += 1
    return vowels_count

def count_consonants(text):
    """Count the number of consonants in the text"""
    consonant_count = 0
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    for char in text:
        if char.lower() in vowel_list:
            continue
        elif char.isalpha():
            consonant_count += 1
    return consonant_count

def count_sentences(text):
    """Count the number of sentences in the text"""
    sentence_count = 0
    for char in text:
        if char == '.':
            sentence_count += 1
    return sentence_count

def count_avg_wpm(text):
    """Count the average words per sentence"""
    wpm = count_white_space(text) / count_sentences(text)
    return wpm 

def main():
    """Read in user input as a txt file and call counting functions
    and print results"""
    txt_file = input("Enter name of text file: ")
    with open(txt_file, 'r') as raw_text:
        text = raw_text.read()
        chars = count_chars(text)
        upper_chars = count_upper_chars(text)
        lower_chars = count_lower_chars(text)
        digits = count_digits(text)
        white_space = count_white_space(text)
        vowels = count_vowels(text)
        consonants = count_consonants(text)
        sentences = count_sentences(text)
        avg_wpm = count_avg_wpm(text)
        print(f"""
Statistics for file: {txt_file}

Characters: {chars}
Upper case: {upper_chars}
Lower case: {lower_chars}
Digits: {digits}
White space: {white_space}
Vowels: {vowels}
Consonants: {consonants}
Sentences: {sentences}
Average words per sentence: {avg_wpm}""")


if __name__ == '__main__':
    main()

