class Solution:
    def mergeTwoLists(self, firstList, secondList):
        return firstList + secondList

a = [1,2,3]
b = [1,4,5]

sol = Solution()
print(sorted(sol.mergeTwoLists(a, b)))