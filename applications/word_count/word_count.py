
ignored = {
    '"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', "|", '[', ']', '{', '}', '(', ')', '*', '^', '&'
}


def word_count(s):
    wordCache = {}

    def word_count_inner(s):
        # Your code here
        s = s.lower()
        for char in s:
            if char in ignored:
                s = s.replace(char, '')
        s = s.split()

        for word in s:
            if word not in wordCache:
                wordCache[word] = 1
            else:
                wordCache[word] += 1

        return wordCache

    return word_count_inner(s)

    



if __name__ == "__main__":
    print(word_count("Hello; ====[ This is fixed? ]"))    
    print(word_count("Hello      hello"))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))