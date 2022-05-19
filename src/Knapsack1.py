# 0-1 Knapsack Problem
# Given weights and values of n items, put these items in a knapsack of 
# capacity W to get the maximum total value in the knapsack.

# Solution 1: 2d DP
# dp[i][j]: Maximum total value of objects selected from 0 to i 
#           in bag with capacity = j
def Knapsack(W, weights, values):
    N = len(weights)
    dp = [[0 for _ in range(W + 1)] for _ in range(N)]
    for j in range(weights[0], W + 1):
        dp[0][j] = values[0]
    # the order of i and j can be changed
    for i in range(1, N):
        for j in range(1, W + 1):
            if weights[i] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], values[i] + dp[i - 1][j - weights[i]])
    return dp[N - 1][W]

# Solution 2: 1d DP
# dp[j]: Maximum total value in bag with capacity = j
def KnapsackOptimizeSpace(W, weights, values):
    N = len(weights)
    dp = [0 for _ in range(W + 1)]
    # the order of i and j CANNOT be changed
    for i in range(N):
        for j in range(W, weights[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
    return dp[W]

# Test cases
W = 4
weights = [1, 3, 4]
values = [15, 20, 30]
print(Knapsack(W, weights, values))
print(KnapsackOptimizeSpace(W, weights, values))