import random
# Key: [followup1, followup2, followup3]
# Read in all the words in one go

# uniqueWords = {
#     "Hello": ['there', 'tyler', '?']
# }


def nextWord(word):
    return random.choice(list(uniqueWords.keys()))


with open("C:\\Users\\tyler\\Documents\\github\\cs-module-project-hash-tables\\applications\\markov\\input.txt") as f:
    # words = f.read()
    wordArray = {}
    for line in f:
        line = line.split()
        for word in line:
            wordArray[word] = word
    print(wordArray)
        
    print(wordArray)

        
    # words = words.split()
    # print(words)
    # uniqueWords = {}

    # for i in range(len(words) - 1):
    #     if words[i] not in uniqueWords:
    #         uniqueWords[words[i]] = [words[i+1]]
    #     else:
    #         uniqueWords[words[i]].append(words[i + 1])
    # # print(uniqueWords)

    # sentence = ''
    # for i in range(15):
    #     word = random.choice(list(uniqueWords.keys()))
    #     sentence += word + " "
    #     word = nextWord(word)

    # sentence[0].upper()
    # sentence[len(sentence)] = '.'

    # print(sentence)



# TODO: analyze which words can follow other words
# Your code here


# TODO: construct 5 random sentences
# Your code here





