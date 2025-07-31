def circularArrayRotation(a, k, queries):
    
    result = []
    k = k % len(a)

    a = a[-k:] + a[:-k]

    for querie in queries:
        result.append(a[querie])
    return result

if __name__ == '__main__':

    k = int(input("Enter the number of rotation count: "))

    q = int(input("Enter what position you want after rotation: "))

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    print(result)