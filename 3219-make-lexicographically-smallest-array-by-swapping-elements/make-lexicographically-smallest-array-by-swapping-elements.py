class Solution:
    def lexicographicallySmallestArray(
        self,
        nums: List[int],
        limit: int
    ) -> List[int]:
        n = len(nums)

        a = sorted(
            (value, index)
            for index, value in enumerate(nums)
        )

        ans = [0] * n

        l = 0

        while l < n:
            r = l

            while (
                r + 1 < n
                and a[r + 1][0] - a[r][0] <= limit
            ):
                r += 1

            indices = sorted(
                a[i][1]
                for i in range(l, r + 1)
            )

            for i in range(l, r + 1):
                ans[indices[i - l]] = a[i][0]

            l = r + 1

        return ans