# OA-1 Find Password Strength 

# def addSet(curSet, c):
#     if c in curSet:
#         curSet[c] += 1
#     else:
#         curSet[c] = 1
#     return curSet

# def dfs(s, startIndex, curSet):
#     if startIndex == len(s):
#         return len(curSet)
#     for i in range(startIndex, len(s)):
#         return dfs(s, i + 1, curSet.add(s[i])) + dfs(s, i + 1, curSet)

# Solution 1: O(n^2)
# def findPasswordStrength(password):
#     result = 0
#     for i in range(len(password)):
#         sub = set()
#         for j in range(i, len(password)):
#             sub.add(password[j])
#             result += len(sub)
#     return result

# Solution 2: DP
# index: {(character, index)} save the last index of character
# dp[i]: strengh of password[0 : i + 1] 
# dp[i] = dp[i - 1] + (i + 1) - (index[password[i]] + 1)
def findPasswordStrength(password):
    dp = [1] * len(password)
    index = {password[0]: 0}
    for i in range(1, len(password)):
        dp[i] = dp[i - 1] + i + 1
        if password[i] in index:
            dp[i] = dp[i] - (index[password[i]] + 1)
        index[password[i]] = i
    return sum(dp)

####test
print(findPasswordStrength("good"))
print(findPasswordStrength("test"))
print(findPasswordStrength("abc"))