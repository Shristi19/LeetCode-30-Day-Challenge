

# Function to find profit
def solve(N, M, cp, sp) :
    # Calculating profit
    # for each gadget
    profit = [sp[i]-cp[i] for i in range(0,N)]

    # sort the profit array
    # in decending order
    profit.sort(reverse = True)

    max_profit = sum(profit[:M])

    return max_profit

# Driver Code
if __name__ == "__main__" :

    N, M = 5, 3
    CP = [5, 10, 35, 7, 23]
    SP = [11, 10, 0, 9, 19]

    # function calling
    print(solve(N, M, CP, SP))


