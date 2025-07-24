# n = 9
# scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]

def breakingRecords(scores):
    min_score = scores[0]
    max_score = scores[0]
    min_count = 0
    max_count = 0

    for score in scores[1:]:
        
        if score < min_score:
            min_score = score
            min_count += 1
            print(min_count)
        elif score > max_score:
            max_score = score
            max_count += 1
            print(max_count)
        
    return max_count,min_count


if __name__ == "__main__":

    n = int(input("Enter array length: ").strip())

    scores = list(map(int, input().rstrip().split()))


    result = breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1])

    print(result)