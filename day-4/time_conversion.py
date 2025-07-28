# s = 07:05:45PM

def timeConversion(s):

    period = s[-2:]
    hour = int(s[:2])
    minute = s[3:5]
    second = s[6:8]

    if period == "PM":
        if hour != 12:
            hour = 12 + hour
    else:
        if hour == 12:
            hour = 0

    return f"{hour:02}:{minute}:{second}"

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)
