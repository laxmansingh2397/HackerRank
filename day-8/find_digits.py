def findDigits(n):
    str_n = str(n)
    count = 0
    for number in str_n:
        if number != '0' and n %  int(number) == 0:
            count += 1
    
    return count



if __name__ == '__main__':

    n = int(input().strip())

    result = findDigits(n)

    print(result)
