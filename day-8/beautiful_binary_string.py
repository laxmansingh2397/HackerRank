def beautifulBinaryString(b):
    
    count = 0
    i = 0 
    while i <= len(b) - 2:
        if b[i:i+3] == "010":
            count += 1
            i += 3
        else:
            i += 1
    return count

if __name__ == '__main__':

    b = input()

    result = beautifulBinaryString(b)

    print(result)