def twoStrings(s1, s2):
    
    for word in s1:
        if word in s2:
            return "YES"
    
    return "NO"



if __name__ == '__main__':

    s1 = input()

    s2 = input()

    result = twoStrings(s1, s2)

    print(result)
