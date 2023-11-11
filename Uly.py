with open('input.txt', encoding='utf8') as f_in:
    nmb_snt = f_in.readline()
    text = f_in.read()

words = text.split()

unique = []
for word in words:
    if word not in unique:
        unique.append(word)
print('unique = ', unique)

for i in range(len(unique)-1):
    next_words = []
    temporary = words
    while temporary.count(unique[i]) > 0:
        ind = temporary.index(unique[i])
        next_words.append(temporary[ind + 1])
        temporary = temporary[ind + 1:]

    print(unique[i], next_words )



