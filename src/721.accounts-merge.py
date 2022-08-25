#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Build nodes and adjacent dict
        # nodes = {email: acct[0] for acct in accounts for email in acct[1:]}
        nodes = {email for acct in accounts for email in acct[1:]}
        adjacent = {node: set() for node in nodes}
        for account in accounts:
            for email in account[2:]:
                adjacent[account[1]].add(email)
                adjacent[email].add(account[1])
        
        # # dfs
        # def dfs(cur, emails):
        #     for neighbor in adjacent[cur]:
        #         if neighbor in nodes:
        #             emails.append(neighbor)
        #             del nodes[neighbor]
        #             dfs(neighbor, emails)
        
        # results = []
        # while nodes:
        #     email, name = nodes.popitem()
        #     emails = [email]
        #     dfs(email, emails)
        #     emails.sort()
        #     results.append([name] + emails)
        
        # return results

        # cleaner dfs
        def dfs(cur, emails):
            for neighbor in adjacent[cur]:
                if neighbor in nodes:
                    emails.append(neighbor)
                    nodes.remove(neighbor)
                    dfs(neighbor, emails)

        results = []
        for account in accounts:
            name = account[0]
            email = account[1]
            if email in nodes:
                nodes.remove(email)
                emails = [email]
                dfs(email, emails)
                results.append([name] + sorted(emails))
        return results
# @lc code=end

