

def catAndMouse(x, y, z):

    if abs(x - z) < abs(y -z):
        return "Cat A"
    elif abs(x - z) == abs(y - z):
         return "Mouse C"
    else:
         return "Cat B"

if __name__ == '__main__':

        x = int(input("Enter Cat A position: "))

        y = int(input("Enter Cat B position: "))

        z = int(input("Enter Mouse postion: "))

        result = catAndMouse(x, y, z)

        print(result)