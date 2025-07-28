# n = 3

def viralAdvertising(n):
    i = 0
    total_liked = 0
    shared = 5
    while i < n:        
        liked = shared // 2
        total_liked += liked
        shared = liked * 3
        i += 1

    return total_liked

if __name__ == '__main__':
    
    n = int(input().strip())

    result = viralAdvertising(n)

    print(result)
    