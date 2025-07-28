def minimumNumber(n, password):
    digit = False
    lower = False
    upper = False
    special = False
    special_characters = "!@#$%^&*()-+"
    
    for char in password:
        if char.islower():
            lower = True
        elif char.isupper():
            upper = True
        elif char.isdigit():
            digit = True
        elif char in special_characters:
            special = True
    
    type_missing = 0

    if not digit:
        type_missing += 1
    if not lower:
        type_missing += 1
    if not upper:
        type_missing += 1
    if not special:
        type_missing += 1
    
    return max(type_missing, 6 - n)

    
if __name__ == '__main__':

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    print(answer)