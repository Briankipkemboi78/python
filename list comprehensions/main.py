import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')



nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

user_name = input("Please enter your name: \n").upper()
splitted_name = list(user_name)


your_name = {letter: nato_dict[letter] for letter in splitted_name if letter in nato_dict}

print(your_name)

