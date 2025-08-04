# a = 1 1 2 2 4 4 5 5 5 


def pickingNumbers(a):

    a.sort()
    max_length = 0

    for i in range(len(a)):
        count = 1
        for j in range(i + 1, len(a)):
            if abs(a[j] - a[i]) <= 1:
                count += 1
            else:
                break
        
        max_length = max(max_length,count)
    
    return max_length
        
    



if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(result)