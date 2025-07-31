
def pangrams(s):
    new_s = "".join(s.lower().split())
    set_s = set(new_s)
    if len(set_s) == 26:
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':

    s = input()

    result = pangrams(s)

    print(result)
