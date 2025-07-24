# n = 5
# arr = [4,5,3,7,2]

def quickSort(arr):
    # Write your code here
    left = []
    equal = arr[0]
    right = []

    for number in arr[1:]:
        
        if number > equal:
            right.append(number)
        else:
            left.append(number)
    
    return left + [equal] + right

if __name__ == '__main__':
    
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)
    
    print(result)