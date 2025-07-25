# x1 = 0
# v1 = 2
# x2 = 5
# v2 = 3

def kangaroo(x1, v1, x2, v2):

    if (v1 < v2):
        return "NO"
    
    if v1 == v2:
        return "YES" if x1 == x2 else "NO"
    
    if (x2 - x1) * (v1 - v2) < 0:
        return "NO"
    
    if (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":

    result = kangaroo(0,2,5,3)

    print(result)
