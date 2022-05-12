# Python3 program to find maximum
# achievable value with a knapsack
# of weight W and multiple instances allowed.

# Returns the maximum value
# with knapsack of W capacity
def unboundedKnapsack(W, n, val, wt):
    # dp[i] is going to store maximum
    # value with knapsack capacity i.
    dp = [[0 for i in range(W + 1)] for j in range(n + 1)]

    ans = 0

    # Fill dp[] using above recursive formula
    for j in range(n + 1):
        currentWeight = wt[j - 1]
        currentValue = val[j - 1]
        for i in range(W + 1):
            if currentWeight <= i:
                dp[j][i] = max(dp[j - 1][i], dp[j][i - currentWeight] + currentValue)
    return dp[n][W]


# Driver program
W = 100
val = [10, 30, 20]
wt = [5, 10, 15]
n = len(val)

print(unboundedKnapsack(W, n, val, wt))

# This code is contributed by Anant Agarwal.
