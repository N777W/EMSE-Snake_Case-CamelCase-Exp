"""Getting test data comparing snake_case and CamelCase"""
import random
import time
import pandas as pd


print("How many? (number should be even)")
num_of_test = int(input())
if num_of_test % 2 != 0:
    num_of_test += 1

print("Starting in")
print("....3")
time.sleep(1)
print("....2")
time.sleep(1)
print("....1")
time.sleep(1)
print("starting now!")
print(" ")

with open("wordsSnake_Case.txt", encoding="utf-8") as file:
    words_S = file.readlines()

with open("wordsCamelCase.txt", encoding="utf-8") as file:
    words_C = file.readlines()

COUNTER = 0

data = pd.DataFrame(columns=["Index", "Word", "Seconds", "W/F", "length"])


def get_word_pair_length(word_pair):
    """gets word pair length for snake_case"""
    words = word_pair.split("_")
    return len(words)


def get_word_pair_length_camel_case(word_pair):
    """gets word pair length for CamelCase"""
    words = []
    current_word = ""
    for char in word_pair:
        if char.isupper() and current_word:
            words.append(current_word)
            current_word = char
        else:
            current_word += char
    if current_word:
        words.append(current_word)
    return len(words)


while COUNTER < num_of_test:
    wordCC = random.choice(words_C)
    wordSC = random.choice(words_S)
    if COUNTER % 2 == 0:
        print(" ")
        print("Word :", wordCC)
        print("Enter the number of word pairs:")
        start_time = time.time()
        user_input = input()
        end_time = time.time()
        elapsed_time = end_time - start_time
        elapsed_time = round(elapsed_time, 2)
        if int(user_input) == get_word_pair_length_camel_case(wordCC):
            print("")
            print("Correct answer!")
            print("Time taken:", elapsed_time, "seconds")
            print("___________________")
            data = pd.concat(
                [
                    data,
                    pd.DataFrame(
                        {
                            "Index": [1],
                            "Word": [wordCC],
                            "Seconds": [elapsed_time],
                            "W/F": "True",
                            "length": get_word_pair_length_camel_case(wordCC),
                        }
                    ),
                ],
                ignore_index=True,
            )
        else:
            print("Incorrect answer!")
            data = pd.concat(
                [
                    data,
                    pd.DataFrame(
                        {
                            "Index": [1],
                            "Word": [wordCC],
                            "Seconds": [elapsed_time],
                            "W/F": "False",
                            "length": get_word_pair_length_camel_case(wordCC),
                        }
                    ),
                ],
                ignore_index=True,
            )

    if COUNTER % 2 != 0:
        print(" ")
        print("Word :", wordSC)
        print("Enter the number of word pairs:")
        start_time = time.time()
        user_input = input()
        end_time = time.time()
        elapsed_time = end_time - start_time
        elapsed_time = round(elapsed_time, 2)
        if int(user_input) == get_word_pair_length(wordSC):
            print(" ")
            print("Correct answer!")
            print("Time taken:", elapsed_time, "seconds")
            print("___________________")
            data = pd.concat(
                [
                    data,
                    pd.DataFrame(
                        {
                            "Index": [2],
                            "Word": [wordSC],
                            "Seconds": [elapsed_time],
                            "W/F": "True",
                            "length": get_word_pair_length(wordSC),
                        }
                    ),
                ],
                ignore_index=True,
            )
        else:
            print("Incorrect answer!")
            data = pd.concat(
                [
                    data,
                    pd.DataFrame(
                        {
                            "Index": [2],
                            "Word": [wordSC],
                            "Seconds": [elapsed_time],
                            "W/F": "False",
                            "length": get_word_pair_length(wordSC),
                        }
                    ),
                ],
                ignore_index=True,
            )
    COUNTER += 1
FILENAME = "word_list.xlsx"
data.to_excel(FILENAME, index=False)
print(f"Data saved to {FILENAME}")
