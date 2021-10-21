from typing import List


class Solution:
    def calc_water_level(
        self, current_height: int, smallest_container_height: int
    ) -> int:
        if smallest_container_height <= current_height:
            return 0
        return smallest_container_height - current_height

    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_left = 0
        max_right = 0
        total = 0
        while i != j:
            if height[i] > height[j]:
                total += self.calc_water_level(height[j], max_right)
                max_right = max(max_right, height[j])
                j -= 1
            else:
                total += self.calc_water_level(height[i], max_left)
                max_left = max(max_left, height[i])
                i += 1
        return total


solution = Solution()
print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
