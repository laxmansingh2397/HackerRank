

def jimOrders(orders):
    serving_with_index = [(sum(order), i+1) for i, order in enumerate(orders)]

    serving_with_index.sort(key=lambda x:x[0])

    result = [order_index for serving_time,order_index in serving_with_index]

    return result 
        

if __name__ == '__main__':

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    print(result)