# 20 23 6

def beautifulDays(i, j, k):
    count = 0

    for day in range(i, j + 1):
        reverse_day = int(str(day)[::-1])
        if abs(day - reverse_day) % k == 0:
            count += 1
    
    return count

if __name__ == '__main__':

    i = int(input("Enter the starting day number: "))

    j = int(input("Enter the ending day number: "))

    k = int(input("Enter the divisor: "))

    result = beautifulDays(i, j, k)

    print(result)
# Write your code here