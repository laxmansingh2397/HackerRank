def introTutorial(V, arr):
    # Write your code here
    
    return arr.index(V)

if __name__ == '__main__':

    V = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    print(result)