
def no_dups(s):

    s = s.split()
    s = list(dict.fromkeys(s))

    fixed = ''
    for i in range(len(s)):
        if i < len(s) - 1:
            fixed += s[i] + " "
        else:
            fixed += s[i]

    return fixed
        



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))