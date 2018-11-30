"""
https://pronouncing.readthedocs.io/en/latest/tutorial.html#counting-syllables
"""
import pronouncing


with open("word.list") as f:
    words = f.read().splitlines()

# print(len(words))

for word in words:
    # print(word)
    pronunciation_list = pronouncing.phones_for_word(word)
    # print(pronunciation_list)
    try:
        syllables = pronouncing.syllable_count(pronunciation_list[0])
    except IndexError:
        continue
    if 1 <= syllables <= 2:
        print(word)
