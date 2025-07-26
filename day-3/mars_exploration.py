
# s = SOSSPSSQSSOR

def marsExploration(s):
    
    expected = "SOS" * (len(s) // 3)
    total = 0

    for i in range(len(s)):
        if s[i] != expected[i]:
            total += 1
    
    return total
    


if __name__ == '__main__':
    
    s = input()

    result = marsExploration(s)

    print(result)