'''
Кнопова Анна 60
Балан Каролина 60
Шилкова Ульяна 50
'''

import random

with open('input.txt', encoding='utf8') as f_in:
    n = int(f_in.readline())
    text = f_in.read()

words = text.split()

unique = []
for word in words:
    if word not in unique:
        unique.append(word)

dict_words = {}
for i in range(len(unique)-1):
    next_words = []
    temporary = words
    while temporary.count(unique[i]) > 0:
        ind = temporary.index(unique[i])
        next_words.append(temporary[ind + 1])
        temporary = temporary[ind + 1:]

    dict_words[unique[i]] = next_words

bred = ''
for j in range(n):
    bred_sentence = ''
    a = 0
    while a < 1:
        first_wrd = random.choice(unique)
        if first_wrd[0].isupper():
            a += 1
            bred_sentence += first_wrd + ' '
            break

    count_words = 1
    k = 0
    next_word = first_wrd
    while k < 1:
        followings = dict_words.get(next_word)
        next_word = random.choice(followings)
        bred_sentence += next_word + ' '
        count_words += 1
        if count_words == 30:
            bred_sentence = bred_sentence[:-1]
            bred_sentence += '. '
            break
        k = bred_sentence.count('.') + bred_sentence.count('!') + bred_sentence.count('?')

    bred += bred_sentence

print(bred)
