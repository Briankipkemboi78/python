import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word:").upper()

try:
    output_list = [nato_dict[letter] for letter in word]
except KeyError:
    print("Sorry only letters allowed")

print(output_list)

