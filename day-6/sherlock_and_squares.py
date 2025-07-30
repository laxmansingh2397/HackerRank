import math

def squares(a, b):
    start = math.ceil(math.sqrt(a))
    end = math.floor(math.sqrt(b))

    squares = [i**2 for i in range(start, end + 1)]
    return len(squares)


if __name__ == '__main__':

    a = int(input("Enter the start range: "))

    b = int(input("Enter the end range: "))

    result = squares(a, b)

    print(result)
