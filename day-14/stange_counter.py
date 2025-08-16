
def strangeCounter(t):

    # counter = []

    # initial = 3
    # current_initial = initial
    # for i in range(t):
    #     if current_initial == 1:
    #         counter.append(current_initial)
    #         initial = initial * 2
    #         current_initial = initial
    #     else:
    #         counter.append(current_initial)
    #         current_initial = current_initial - 1

    # return counter[t - 1]

    cycle_start = 1
    cycle_val = 3

    # Find cycle that contains time t
    while t > cycle_start + cycle_val - 1:
        cycle_start += cycle_val
        cycle_val *= 2

    # Value at time t is what's left in this cycle
    return cycle_val - (t - cycle_start)




if __name__ == '__main__':

    t = int(input().strip())

    result = strangeCounter(t)

    print(result)
