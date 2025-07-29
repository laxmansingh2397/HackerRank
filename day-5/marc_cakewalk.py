



def marcsCakewalk(calorie):

    minimum_miles = 0
    calorie.sort(reverse=True)
    print(calorie)
    for i in range(len(calorie)):
        minimum_miles += (2 ** i) * calorie[i]

    return minimum_miles

if __name__ == '__main__':

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    print(result)