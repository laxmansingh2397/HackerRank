
# s = "aaabccddd"

def superReducedString(s):
    
    result = []

    for char in s:
        if result and result[-1] == char:
            result.pop()
        else:
            result.append(char)
    
    return "".join(result) if result else "Empty String"

if __name__ == "__main__":
    
    s = input("Enter a string: ")

    result = superReducedString(s)

    print(result)