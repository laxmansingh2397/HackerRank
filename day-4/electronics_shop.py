
# b = 60
# keyboard = [40,50,60]
# drives = [5,8,12]


def getMoneySpent(keyboards, drives, b):
    
    possible_buy = -1

    for keyboard in keyboards:
        for drive in drives:
            if keyboard + drive <= b:
                can_buy = keyboard + drive
                possible_buy = max(possible_buy, can_buy)

    
    return possible_buy

    



if __name__ == '__main__':

    b = int(input("Enter your total budget: "))

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(moneySpent)