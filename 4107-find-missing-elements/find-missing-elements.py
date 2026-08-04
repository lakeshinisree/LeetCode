class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        present = [False] * 101

        mini = min(nums)
        maxi = max(nums)

        for num in nums:
            present[num] = True

        ans = []

        for i in range(mini, maxi + 1):
            if not present[i]:
                ans.append(i)

        return ans