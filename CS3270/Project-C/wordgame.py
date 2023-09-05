from random import choice, shuffle
from collections import Counter
import sys

def main():
    with open("words.txt", 'r') as word_list:
        word_list = word_list.readlines()
        # database = HashMap()
        group_words_by_length = {}
        for word in word_list:
            word = word.strip()
            #groups the words by their length
            group_words_by_length.setdefault(len(word), list())
            group_words_by_length[len(word)].append(word)
            # database.add_new(word)
        word_range = tuple(input("Enter the range of word lengths (low,high):").split(','))
        # choosing a random word and scrambling it

        try:
            random_word = list(sys.argv[1])
        except:
            random_word = list(choice(group_words_by_length[int(word_range[1])]))

        shuffle(random_word)
        random_word = ''.join(random_word)
        # random_word =("esaywa")
        # print(random_word)
        list_of_words = []
        final_list = []
        for i in range(int(word_range[0]), int(word_range[1])+1):
            list_of_words.extend(group_words_by_length[i])
        test_word = Counter(random_word)
        for word in list_of_words:
            new_word = Counter(word)
            if all(letters in list(test_word) for letters in list(new_word)) and all(new_word[letter] <= test_word[letter] for letter in new_word):
                final_list.append(word)
        
        test = {}
        for i in final_list:
            test.setdefault(len(i), list())
            test[len(i)].append(i)




        # print(test)

        guesses = {}

        for key in test:
            guesses[key] = test[key].copy()


        for key in guesses:
            for value in guesses[key]:
                guesses[key][guesses[key].index(value)] = "-"*len(value)


        win = False
        player_guess = ""

        another_key = False
        

        while (win == False and player_guess != 'q'):
            pass_key = False
            random_word = list(random_word)
            shuffle(random_word)
            random_word = ''.join(random_word)
            print(random_word + ":\n")
            for key in test:
                for value in test[key]:
                    if guesses[key][test[key].index(value)] == value:
                        continue
                    elif (player_guess == value):
                        guesses[key][test[key].index(value)] = value
                        pass_key = True

                    else:
                        guesses[key][test[key].index(value)] = "-"*len(value)
                print(guesses[key])

            if another_key == False:
                another_key = True
            else:
                if pass_key == True:
                    print("Correct")
                else:
                    print("Incorrect!")

            if guesses == test:
                win = True
            else:
                player_guess = input("Enter a guess: ")
                print("")
                print("")
        

        final_list = []
        if win == True:
            print("You win!!!\n\n")
        for key in test:
            for value in test[key]:
                final_list.append(value)
        print(final_list)
if __name__ == "__main__":
    main()


