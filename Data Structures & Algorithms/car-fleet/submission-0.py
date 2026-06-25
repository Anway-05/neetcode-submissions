class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_spd=sorted(zip(position,speed))
        time=[]
        for x,y in pos_spd:
            time.append((target-x)/y)
        stack=[]
        for x in time:
           stack.append(x)
        n_fleet=0
        while stack:
            temp1=stack.pop()
            while stack and stack[-1]<=temp1:
                stack.pop()
            n_fleet+=1
        return n_fleet