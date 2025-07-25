
# arr = 1 4 4 4 5 3

def migratoryBirds(arr):
    
    higher_frequency = []
    type_count = 0
    unique_bird = set(arr)

    for bird_type in unique_bird:
        count = arr.count(bird_type)
        if count > type_count:
            type_count = count
            higher_frequency = [bird_type]
        elif count == type_count:
                higher_frequency.append(bird_type)

    print(higher_frequency)
    return min(higher_frequency)

if __name__ == '__main__':


    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)
