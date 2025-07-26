
# k = 3
# ar = 1 3 2 6 1 2

def divisibleSumPairs(k, ar):

    pairs = []
    for i in range(len(ar)):
        for j in range(i+1,len(ar)):
            if ((ar[i] + ar[j]) % k == 0):
                pairs.append([ar[i],ar[j]])

    return len(pairs)

if __name__ == '__main__':
    
    k = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(k, ar)

    print(result)