

def chocolateFeast(n, c, m):
    
    chocolates = n // c
    wrapper = chocolates

    while wrapper >= m:
        extra = wrapper // m
        chocolates += extra
        wrapper = extra + (wrapper % m)

    return chocolates

if __name__ == '__main__':

    n = int(input())

    c = int(input())

    m = int(input())

    result = chocolateFeast(n, c, m)

    print(result)
