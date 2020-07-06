import random
# Key: [followup1, followup2, followup3]
# Read in all the wordArray in one go

# uniqueWordArray = {
#     "Hello": ['there', 'tyler', '?']
# }


ignored = {
    '"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', "|", '[', ']', '{', '}', '(', ')', '*', '^', '&'
}


def nextWord(word):
    return random.choice(list(uniqueWordArray.keys()))


with open("C:\\Users\\tyler\\Documents\\github\\cs-module-project-hash-tables\\applications\\markov\\input.txt") as f:
    wordArray = []
    for line in f:
        line = line.split()
        for word in line:
            for char in word:
                if char in ignored:
                    word = word.replace(char, '')

            wordArray.append(word)
    

        

    uniqueWordArray = {}

    for i in range(len(wordArray) - 1):
        if wordArray[i] not in uniqueWordArray:
            uniqueWordArray[wordArray[i]] = [wordArray[i+1]]
        else:
            uniqueWordArray[wordArray[i]].append(wordArray[i + 1])

    # print(uniqueWordArray)

    sentence = ''
    for i in range(15):
        word = random.choice(list(uniqueWordArray.keys()))
        if i == 0:
            word = word.capitalize()
        sentence += ' ' + word
        word = nextWord(word)

    sentence = sentence + '.'
    # sentence.append('.')

    print(sentence)





