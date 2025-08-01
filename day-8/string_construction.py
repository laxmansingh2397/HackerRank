def stringConstruction(s):
    
    set_s = set(s)

    return len(set_s)


if __name__ == '__main__':

    s = input()

    result = stringConstruction(s)

    print(result)
