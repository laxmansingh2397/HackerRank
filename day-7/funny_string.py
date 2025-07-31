def funnyString(s):
    reverse_s = s[:: -1]

    for word in range(len(reverse_s) - 1):
        difference_s = abs(ord(reverse_s[word]) - ord(reverse_s[word + 1]))
        difference_reverse_s = abs(ord(s[word]) - ord(s[word + 1]))
        if  difference_s != difference_reverse_s:
            return "Not Funny"
        
    return "Funny"

if __name__ == '__main__':
        s = input()

        result = funnyString(s)

        print(result)
