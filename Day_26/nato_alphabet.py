
import pandas


nato_csv = pandas.read_csv("Day_26/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for index,row in nato_csv.iterrows()}

word = input("Enter a word: ").upper()

nato_codes = [nato_dict[char] for char in word]
print(nato_codes)
