import pandas
data=pandas.read_csv('nato_phonetic_alphabet.csv')

#TODO 1. Create a dictionary in this format:
nato_dict={row.letter:row.code for (index,row) in data.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
inp=input('Enter your word: ').upper()
user_phonetic_code= [nato_dict[let] for let in inp if let in nato_dict]
print(user_phonetic_code)
