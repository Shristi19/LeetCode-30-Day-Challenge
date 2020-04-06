llist=[1,2,3,4,5]


def logic(prices):
    answer=[]
    n=len(prices)

    if n==1:
        return 0

    i=0

    while i < n-1:

        while i < n-1 and prices[i+1] <= prices[i]:
            i+=1
        if i== n-1:
            break
        buy=prices[i]
        i+=1


        while i < n and prices[i] >= prices[i-1]:
            i+=1
        sell=prices[i-1]

        answer.append(sell-buy)

    return sum(answer)

print(logic(llist))



