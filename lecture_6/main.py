import re

with open("lorem.txt", "r", encoding='utf-8') as file:
    text = file.read()
    data = re.split(r'[.,;!? \n]', text.lower())
    data = list(filter(lambda x: x != "", data))
    print(f'Number of words: {len(data)}')
    unique_words = set(data)
    print(f'Number of unique words: {len(unique_words)}')
    counter = {}
    for i in unique_words:
        counter[i] = data.count(i)
    counter = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
    print("Top 10 words:")
    for i, key in enumerate(counter):
        if i == 10:
            break
        print(f'{key}: {counter[key]}')

    print(f'Count: {counter.get(input("Enter word to count: "), "Word not found")}')

    letters = {}
    for i in text.lower():
        if i.isalpha():
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1

    letters = dict(sorted(letters.items(), key=lambda x: x[1], reverse=True))
    print("Amount of each letter in text:")
    for key in letters:
        print(f'{key}: {letters[key]}')

    sentences = re.split(r'[.!?\n]', text)
    word_regex = re.compile(r'[a-zA-Z]+')
    sts = {}
    for i, sen in enumerate(sentences):
        for w in set(word_regex.findall(sen)):
            try:
                sts[w].add(i)
            except BaseException:
                sts[w] = {i}

    max_count = 0
    max_words = []
    for i, val_i in enumerate(sts):
        for u, val_u in enumerate(sts):
            if i <= u:
                break
            if len(sts[val_i].intersection(sts[val_u])) > max_count:
                max_count = len(sts[val_i].intersection(sts[val_u]))
                max_words = [val_i, val_u]

    print(f'Maximum number of sentences with common words: {max_count}')
    print(f'Words: {max_words[0]} and {max_words[1]}')

