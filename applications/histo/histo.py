# Your code here

ignored = {
    "?","'",'"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', "|", '[', ']', '{', '}', '(', ')', '*', '^', '&', '!'
}

with open("C:\\Users\\tyler\\Documents\\github\\cs-module-project-hash-tables\\applications\\histo\\robin.txt") as f:
    chars = {}
    frequencyDict = {}
    for line in f:
        line = line.split()
        for word in line:
            for char in word:
                if char in ignored:
                    word = word.replace(char, '')
                else:
                    char = char.lower()
                    if char not in chars:
                        chars[char] = 1
                    else:
                        chars[char] += 1
                    
            if word not in frequencyDict:
                frequencyDict[word] = 1
            else:
                frequencyDict[word] += 1

    freq = frequencyDict.items()
    freq = sorted(freq, key = lambda x: x[1], reverse=True)

    
    for tup in freq:
        spacing = 17 - len(tup[0])
        # print(f'{tup[0]}' + ((" ")*spacing) + (('#') * tup[1]))

    # print(chars)

    print(len(chars.items()))

    total = 0
    for letter in chars:
        total += chars[letter]

    # print('Total', total)

    for letter in chars:
        chars[letter] = f'{round(chars[letter] / total * 100, 3)}%'

    chars = {k: v for k, v in sorted(chars.items(), key=lambda item: item[1], reverse=True)}
    # chars = sorted(chars, key = lambda x: x[1], reverse=True)
    print(chars)
    





    