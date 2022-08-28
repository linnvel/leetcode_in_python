#
# @lc app=leetcode id=1152 lang=python3
#
# [1152] Analyze User Website Visit Pattern
#

# @lc code=start

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # pattern_dict = {}
        # global max_count, freq_pattern
        # max_count = 0
        # freq_pattern = []
        
        # def smaller_pattern(pattern1, pattern2):
        #     for w1, w2 in zip(pattern1, pattern2):
        #         if w1 == w2:
        #             continue
        #         elif w1 < w2:
        #             return pattern1
        #         else:
        #             return pattern2
        #     return pattern1
        
        # def dfs(user, websites, startIndex, current):
        #     global max_count, freq_pattern
        #     if len(current) == 3:
        #         pattern = tuple(current)
        #         if pattern not in pattern_dict:
        #             pattern_dict[pattern]  = {user}
        #         else:
        #             if user in pattern_dict:
        #                 return
        #             pattern_dict[pattern].add(user)
                    
        #         cur_count = len(pattern_dict[pattern])
        #         if freq_pattern == [] or cur_count > max_count:
        #             max_count = cur_count
        #             freq_pattern = current
        #         elif cur_count == max_count:
        #             freq_pattern = smaller_pattern(freq_pattern, current)
        #         return
            
        #     for i in range(startIndex, len(websites)):
        #         dfs(user, websites, i + 1, current + [websites[i]])
        
        # sorted_index = sorted(range(len(timestamp)), key=lambda k: timestamp[k])
        # user_dict = {user:[] for user in set(username)}
        # for i in sorted_index:
        #     name = username[i]
        #     web = website[i]
        #     user_dict[name].append(web)

        # for user, webs in user_dict.items():
        #     if len(webs) < 3:
        #         continue
        #     dfs(user, webs, 0, [])
        
        # return freq_pattern

        # Cleaner implementation
        from collections import Counter

        def dfs(websites, startIndex, current, result):
            if len(current) == 3:
                result.add(tuple(current))
                return
            
            for i in range(startIndex, len(websites)):
                dfs(websites, i + 1, current + [websites[i]], result)

        user_dict = {user:[] for user in set(username)}
        for name, web, _ in sorted(zip(username, website, timestamp), key=lambda x: x[2]):
            user_dict[name].append(web)

        # use Counter to help count
        # It's simliar with defining a count dict
        pattern_counter = Counter()
        for websites in user_dict.values():
            patterns = set()
            dfs(websites, 0, [], patterns)
            pattern_counter.update(Counter(patterns))
        # sorted can sort tuple/list of strings
        return max(sorted(pattern_counter), key = pattern_counter.get)
        

# @lc code=end