class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        start_pt = 0
        pivot_pt = len(height)-1
        while start_pt < pivot_pt:
            sum_ = 0
            # print(f"start point::: {start_pt}; start height::: {height[start_pt]}")
            # print(f"pivot point::: {pivot_pt}; start height::: {height[pivot_pt]}")
            diff = min(height[start_pt],height[pivot_pt])
            # print(f"diff::: {diff}")
            sum_ = diff * (pivot_pt - start_pt) if pivot_pt - start_pt > 0 else diff
            answer = max(answer,sum_)
            if height[start_pt] < height[pivot_pt]:
                start_pt += 1
            elif height[start_pt] > height[pivot_pt]:
                pivot_pt -=1
            else:
                start_pt += 1
            # print(f"answer for this iteration::: {answer}")
        return answer

input = []
answer = Solution.maxArea(input)
print(answer)