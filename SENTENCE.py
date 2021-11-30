# Program 1:
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input
# ex.
# input: Bahala kayo dyan
# output:
# words: 3
# vowels: 6
# consonants: 8
def display_program():
    print('This program will ask you for a sentence and it will count how many words, vowels, and consonants is in the sentence.')

def get_sentence():
    sentence = (input('Enter a sentence: '))
    return sentence

def count_num_of_words():
    words = sentence.split()
    num_of_words = len(words)
    return num_of_words

def count_num_of_vowels():
    vowels = 'aAeEiIoOuU'
    num_of_vowels = 0
    for c in sentence:
        if c in vowels:
            num_of_vowels = num_of_vowels + 1
    return num_of_vowels

def count_num_of_consonants():
    consonants = 'bBcCdDfFgGhHjJkKlLmMnNñÑpPqQrRsStTvVwWxXyYzZ'
    num_of_consonants = 0
    for c in sentence:
        if c in consonants:
            num_of_consonants = num_of_consonants + 1
    return num_of_consonants

def display_output():
    print('Words:',words)
    print('Vowels:',vowels)
    print('Consonants:',consonants)



display_program() #this will just let the user know what this program is about
sentence = get_sentence() #this will ask the user for a sentence
words = count_num_of_words() #this will count the number of words in the sentence
vowels = count_num_of_vowels() #this will count the number of vovels in the sentence
consonants = count_num_of_consonants() #this will count the number of consonants in the sentence
display_output() #this will display how many words, vowels, and consonants is in the sentence