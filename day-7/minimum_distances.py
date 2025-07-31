def minimumDistances(a):
    last_seen_dict = {}
    min_diff = float('inf')

    for i in range(len(a)):
        if a[i] in last_seen_dict:
            diff = i - last_seen_dict[a[i]]
            min_diff = min(min_diff, diff)
        last_seen_dict[a[i]] = i

    if min_diff != float('inf'):
        return min_diff
    else:
        return -1

if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    print(result)
