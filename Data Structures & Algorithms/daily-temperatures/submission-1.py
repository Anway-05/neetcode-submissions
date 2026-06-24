class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0]*len(temperatures)
        for i,x in enumerate(temperatures):
            while stack and x>temperatures[stack[-1]]:
                result[stack[-1]]=i-stack[-1]
                stack.pop()
            stack.append(i)
        return result