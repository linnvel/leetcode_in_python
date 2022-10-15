#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#

# @lc code=start
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # # Solution 1: Trie
        # trie = {}
        # for product in products:
        #     cur = trie
        #     for c in product:
        #         if c not in cur:
        #             cur[c] = {}
        #         cur = cur[c]
        #     cur["$"] = len(product)

        # def get_words(cur, word, result):
        #     for c in cur.keys():
        #         if c == "$":
        #             result.append(word)
        #         else:
        #             get_words(cur[c], word + c, result)
            
        # results = []
        # cur = trie
        # find = True
        # for i in range(len(searchWord)):
        #     if not find or searchWord[i] not in cur:
        #         find = False
        #         results.append([])
        #         continue
        #     result = []
        #     cur = cur[searchWord[i]]
        #     get_words(cur, searchWord[:i+1], result)
        #     results.append(sorted(result)[:3])
        # return results
        
        # Solution 2: Binary Search
        products.sort()
        l, r = 0, len(products) - 1
        for i in range(len(searchWord)):
            
        
        
# @lc code=end

