class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = {}
        for num in nums:
            if num in visited:
                return True
            else:
                visited[num] = 0
            
        return False
