

def hackerrankInString(s):
    find_sting = "hackerrank"

    n = len(find_sting)

    i = 0

    for char in s:
        if char == find_sting[i]:
            i += 1
            if i == n:
                return "YES"
    
    return "NO"
    
    

if __name__ == '__main__':

    s = input()

    result = hackerrankInString(s)

    print(result)
