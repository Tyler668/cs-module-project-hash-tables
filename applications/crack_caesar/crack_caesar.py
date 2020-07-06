ignored = [
    "\n",' ', ',', 'â', '1', '”', '€', "?", "'", '"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', "|", '[', ']', '{', '}', '(', ')', '*', '^', '&', '!'
]


def exampleSpread():
    refList = ['e', 't', 'a', 'o', 'h', 'n', 'r', 'i', 's', 'd', 'l', 'w',
               'u', 'g', 'f', 'b', 'm', 'y', 'c', 'p', 'k', 'v', 'q', 'j', 'x', 'z']
    return refList


def caesarSpread():
    with open("C:\\Users\\tyler\\Documents\\github\\cs-module-project-hash-tables\\applications\\crack_caesar\\ciphertext.txt") as f:
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
        freq = sorted(freq, key=lambda x: x[1], reverse=True)

        for tup in freq:
            spacing = 17 - len(tup[0])
            # print(f'{tup[0]}' + ((" ")*spacing) + (('#') * tup[1]))


        total = 0
        for letter in chars:
            total += chars[letter]

        # print('Total', total)

        for letter in chars:
            chars[letter] = f'{round(chars[letter] / total * 100, 3)}%'

        chars = {k: v for k, v in sorted(
            chars.items(), key=lambda item: item[1], reverse=True)}

        # chars = sorted(chars, key = lambda x: x[1], reverse=True)
        print('Chars')
        print(chars)
        caesarFreqArray = [key for key in chars.keys()]
        caesarFreqArray.remove('w')
        caesarFreqArray.insert(0, 'w')
        print(caesarFreqArray)

        return caesarFreqArray



normal = list(exampleSpread())
caesar = list(caesarSpread())
decoder = dict(zip(caesar, normal))

def decode(string):

    string = string.lower()
    for i in range(len(ignored)):
        string = string.replace(ignored[i], '')


    # print('decoding:',)
    decodedString = ''
    for char in string:
        decodedString += decoder[char]
    return decodedString
# -----------------------------------



with open("C:\\Users\\tyler\\Documents\\github\\cs-module-project-hash-tables\\applications\\crack_caesar\\ciphertext.txt") as f:
    decoded = ''
    
    for line in f:
        toDecode = line 
        toDecode = toDecode.split()
        newLine = ''
        for word in toDecode:
            newLine += decode(word) + ' '

        decoded += newLine

    print('Decoded:',decoded)
