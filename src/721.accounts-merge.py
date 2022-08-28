#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # # Solution 1: DFS
        # # Build nodes and adjacent dict
        # # nodes = {email: acct[0] for acct in accounts for email in acct[1:]}
        # nodes = {email for acct in accounts for email in acct[1:]}
        # adjacent = {node: set() for node in nodes}
        # for account in accounts:
        #     for email in account[2:]:
        #         adjacent[account[1]].add(email)
        #         adjacent[email].add(account[1])
        
        # # def dfs(cur, emails):
        # #     for neighbor in adjacent[cur]:
        # #         if neighbor in nodes:
        # #             emails.append(neighbor)
        # #             del nodes[neighbor]
        # #             dfs(neighbor, emails)
        
        # # results = []
        # # while nodes:
        # #     email, name = nodes.popitem()
        # #     emails = [email]
        # #     dfs(email, emails)
        # #     emails.sort()
        # #     results.append([name] + emails)
        
        # # return results

        # # cleaner dfs
        # def dfs(cur, emails):
        #     for neighbor in adjacent[cur]:
        #         if neighbor in nodes:
        #             emails.append(neighbor)
        #             nodes.remove(neighbor)
        #             dfs(neighbor, emails)

        # results = []
        # for account in accounts:
        #     name = account[0]
        #     email = account[1]
        #     if email in nodes:
        #         nodes.remove(email)
        #         emails = [email]
        #         dfs(email, emails)
        #         results.append([name] + sorted(emails))
        # return results

        # Solution 2: DFU
        def find(parents, node):
            parent = node
            while isinstance(parents[parent], str):
                parent = parents[parent]
            if isinstance(parents[node], str):
                parents[node] = parent
            return parent
        
        def union(parents, nodea, nodeb):
            parenta = find(parents, nodea)
            parentb = find(parents, nodeb)
            if parenta != parentb:
                if parents[parenta] <= parents[parentb]:
                    parent, child = parenta, parentb
                else:
                    parent, child = parentb, parenta
                parents[parent] += parents[child]
                parents[child] = parent
                
        parents = {}
        merged_map = {}
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                parents[email]  = -1
                merged_map[email] = [name]
        
        for account in accounts:
            email = account[1]
            for neighbor in account[2:]:
                union(parents, email, neighbor)
        
        for email in parents.keys():
            name = merged_map[email]
            parent = find(parents, email)
            merged_map[parent].append(email)
            if parent != email:
                del merged_map[email]
        
        for email in merged_map.keys():
            merged_map[email] = [merged_map[email][0]] + sorted(merged_map[email][1:])
        
        return merged_map.values()
# @lc code=end

