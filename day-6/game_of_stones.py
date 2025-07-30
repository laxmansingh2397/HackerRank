# t = 1 2 3 4 5 6 7 10



def gameOfStones(n):
    
    if n % 7 < 2:
        return "Second"
    else:
        return "First"

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = gameOfStones(n)

        print(result)