#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
# class TreeNode:
#     def __init__(self, value="", children={}, isword=0) -> None:
#         self.value = value
#         self.children = {}  # key: children character, value: children node
#         self.isword = isword

# class Trie:
#     def __init__(self):
#         self.head = TreeNode()

#     def insert(self, word: str) -> None:
#         cur = self.head
#         for c in word:
#             if c not in cur.children:
#                 cur.children[c] = TreeNode(c)
#             cur = cur.children[c]
#         cur.isword = 1

#     def search(self, word: str) -> bool:
#         cur = self.head
#         for c in word:
#             if c not in cur.children:
#                 return False
#             cur = cur.children[c]
#         return cur.isword == 1        

#     def startsWith(self, prefix: str) -> bool:
#         cur = self.head
#         for c in prefix:
#             if c not in cur.children:
#                 return False
#             cur = cur.children[c]
#         return True

# Solution 2: less memory
class Trie:
    def __init__(self):
        self.children = {}

    def insert(self, word: str) -> None:
        cur = self.children
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur["$"] = word

    def search(self, word: str) -> bool:
        cur = self.children
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return "$" in cur and cur["$"] == word        

    def startsWith(self, prefix: str) -> bool:
        cur = self.children
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

