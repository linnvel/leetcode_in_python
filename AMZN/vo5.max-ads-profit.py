# VO-5 Max Ads Profit

def maxProfit(ads, T):
    # 0-1 backpacking
    # dp[j] = max profit with time limit = j
    # dp[j] = max(dp[j], dp[j - time[i]] + profit[i])
    # iteration order: object first, then weight
    dp = [0] * (T + 1)
    n = len(ads)
    for i in range(n):
        for j in range(ads[i][0], T + 1):
            dp[j] = max(dp[j], dp[j - ads[i][0]] + ads[i][1])
    return dp[-1]

def maxPartialProfit(ads, T):
    # Greedy
    ads.sort(key = lambda x: x[0] / x[1])
    profit = 0
    for i in range(len(ads)):
        if T >= ads[i][0]:
            T -= ads[i][0]
            profit += ads[i][1] 
        else:
            ratio = ads[i][0] / ads[i][1]
            profit += T / ratio
            break
    return profit

ads = [[68, 20], [30, 15], [40, 20], [50, 25]]
T = 120
print(maxProfit(ads, T))
print(maxPartialProfit(ads, T))