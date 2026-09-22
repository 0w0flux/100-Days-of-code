import pandas


nato_csv = pandas.read_csv("Day_26/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for index,row in nato_csv.iterrows()}
print(nato_dict)

def test():
    word = input("Enter a word: ").upper()
    try:
        nato_codes = [nato_dict[char] for char in word]
    except KeyError:
        print("Sorry, only letters in the nato alphabet can be used!")
        test()
    else:
        print(nato_codes)

test()