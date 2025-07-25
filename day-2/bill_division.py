# k = 1
# bill = 3 10 2 9
# b = 12


def bonAppetit(bill, k, b):
    
    fair = (sum(bill) - bill[k]) // 2

    if (b == fair):
        print("Bon Appetit")
    else:
        print(abs(b - fair))


if __name__ == "__main__":

    k = int(input("Enter which item you don't want to eat: "))

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    result = bonAppetit(bill, k, b)
    
    print(result)