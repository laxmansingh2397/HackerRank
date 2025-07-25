
# candles = 3 2 1 3

def birthdayCakeCandles(candles):
    max_candles = max(candles)

    return candles.count(max_candles)

if __name__ == '__main__':

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    print(result)