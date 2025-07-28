# k = 4
# height =1 6 3 5 2

def hurdleRace(k, height):
    max_height_need = max(height)

    if max_height_need > k:
        return max_height_need - k
    else:
        return 0    

if __name__ == '__main__':

    k = int(input("Enter your jump height: "))

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    print(result)
