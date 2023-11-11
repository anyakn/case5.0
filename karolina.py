with open('input.txt', encoding='utf8') as f_in:
    nmb_snt = f_in.readline()
    text = f_in.readline()

words = text.split()

unique = []
for word in words:
    if word not in unique:
        unique.append(word)
print('unique = ', unique)