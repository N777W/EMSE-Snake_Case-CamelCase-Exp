import random
import time
import pandas as pd
import openpyxl

print('How many? (number should be even)')
num = int(input())
if(num % 2 != 0):
    num+=1

print('Starting in')
print('....3')
time.sleep(1)
print('....2')
time.sleep(1)
print('....1')
time.sleep(1)
print('starting now!')
print(' ')

with open("wordsSnake_Case.txt") as file:
    words_S = file.readlines()

with open("wordsCamelCase.txt") as file:
    words = file.readlines()

counter = 0

data = pd.DataFrame(columns=['Index','Word', 'Seconds','W/F','length'])

def get_word_pair_length(word_pair):
    words = word_pair.split("_")
    return len(words)

def get_word_pair_length_camel_case(word_pair):
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

while(counter<num):
    wordCC = random.choice(words)
    wordSC = random.choice(words_S)
    if(counter % 2 == 0):
        print(" ")
        print("Word :", wordCC)
        print("Enter the number of word pairs:")
        start_time = time.time()
        user_input = input()
        end_time = time.time()
        elapsed_time = end_time - start_time
        elapsed_time = round(elapsed_time,2)
        if int(user_input) == get_word_pair_length_camel_case(wordCC):
            print("")
            print("Correct answer!")
            print("Time taken:", elapsed_time, "seconds")
            print("___________________")
            data = pd.concat([data, pd.DataFrame({'Index': [1],
                                                  'Word': [wordCC],
                                                  'Seconds': [elapsed_time],
                                                  'W/F': 'True',
                                                  'length': get_word_pair_length_camel_case(wordCC)})]
                             , ignore_index=True)
        else:
            print("Incorrect answer!")
            data = pd.concat([data, pd.DataFrame({'Index': [1],
                                                  'Word': [wordCC],
                                                  'Seconds': [elapsed_time],
                                                  'W/F': 'False','length': get_word_pair_length_camel_case(wordCC)})],
                             ignore_index=True)

    if(counter % 2 != 0):
        print(" ")
        print("Word :", wordSC)
        print("Enter the number of word pairs:")
        start_time = time.time()
        user_input = input()
        end_time = time.time()
        elapsed_time = end_time - start_time
        elapsed_time = round(elapsed_time,2)
        if int(user_input) == get_word_pair_length(wordSC):
            print(" ")
            print("Correct answer!")
            print("Time taken:", elapsed_time, "seconds")
            print("___________________")
            data = pd.concat([data, pd.DataFrame({'Index': [2],
                                                  'Word': [wordSC],
                                                  'Seconds': [elapsed_time],
                                                  'W/F': 'True',
                                                  'length':get_word_pair_length(wordSC)})]
                             , ignore_index=True)
        else:
            print("Incorrect answer!")
            data = pd.concat([data, pd.DataFrame({'Index': [2],
                                                  'Word': [wordSC],
                                                  'Seconds': [elapsed_time],
                                                  'W/F': 'False',
                                                  'length':get_word_pair_length(wordSC)})]
                             , ignore_index=True)
    counter+=1
filename = 'word_list.xlsx'
data.to_excel(filename, index=False)
print(f"Data saved to {filename}")





