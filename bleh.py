#!/usr/bin/python3
# -*-coding:utf-8 -*

from operator import itemgetter
import sys

def map_words(input_file):
    # file = open(input_file, 'r')

    # force the file in encoding utf-8
    file = open(input_file, 'r', encoding='utf-8')

    for line in file:
        line = line.lower()
        line = line.strip()
        words = line.split()
        for word in words:
            yield (word, 1)

def reduce_words(word_pairs):
    current_word = None
    current_count = 0
    word = None

    for word, count in sorted(word_pairs, key=itemgetter(0)):
        if current_word == word:
            current_count += count
        else:
            if current_word:
                yield (current_word, current_count)
            current_count = count
            current_word = word
    if current_word == word:
        yield (current_word, current_count)

def map_reduce(input_file = 'books_cat.txt', output_file = 'output.txt'):
    word_counts = list(reduce_words(list(map_words(input_file))))

    with open(output_file, 'w') as file:
        for word, count in word_counts:
            try: # needj to pass on weird chars
                file.write(f'{word}\t{count}\n')
            except:
                pass
if __name__ == "__main__":
    map_reduce()