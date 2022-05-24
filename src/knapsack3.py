# Bounded Knapsack Problem
# Given weights, amounts and values of n items, put these items in a knapsack of 
# capacity W to get the maximum total value in the knapsack.

# Solution: DP
# dp[j]: Maximum total value of objects in bag with capacity = j

def BoundedKnapsack(W, weights, values, amounts):
    dp = [0] * (W + 1)
    for i in range(len(weights)):
        for k in range(amounts[i]):
            for j in range(W, k * weights[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - k * weights[i]] + k * values[i])
    return dp[W]

# Test cases
W = 10
weights = [1, 3, 4]
values = [15, 20, 30]
amounts = [2, 3, 2]
print(BoundedKnapsack(W, weights, values, amounts))
