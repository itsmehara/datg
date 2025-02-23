# This is for testing purpose sample code.

import nltk
from nltk.corpus import words
import random

nltk.download('words')
word_list = words.words()


def generate_name():
    word1 = random.choice(word_list).capitalize()
    word2 = random.choice(word_list).capitalize()
    return word1 + " " + word2


print(generate_name())  # Example Output: OceanSpark
print(generate_name())  # Example Output: OceanSpark
print(generate_name())  # Example Output: OceanSpark
print(generate_name())  # Example Output: OceanSpark
print(generate_name())  # Example Output: OceanSpark
print(generate_name())  # Example Output: OceanSpark
