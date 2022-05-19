# Unbounded Knapsack Problem
# Given weights and values of n items, put these items in a knapsack of 
# capacity W to get the maximum total value in the knapsack.
# Assume we are allowed to use unlimited number of instances of an item.

# Solution: DP
# dp[j]: Maximum total value of objects in bag with capacity = j

# Iterate over weight first
def UnboundedKnapSack(W, weights, values):
    dp = [0] * (W + 1)
    for i in range(len(weights)):
        for j in range(weights[i], W + 1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
    return dp[W]

# Iterate over item first
def UnboundedKnapSack2(W, weights, values):
    dp = [0] * (W + 1)
    for j in range(W + 1):
        for i in range(len(weights)):
            if j < weights[i]:
                continue
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
    return dp[W]


# Test cases
W = 4
weights = [1, 3, 4]
values = [15, 20, 30]
print(UnboundedKnapSack(W, weights, values))
print(UnboundedKnapSack2(W, weights, values))