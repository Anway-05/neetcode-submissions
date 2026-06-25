class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_spd=sorted(zip(position,speed))
        time=[]
        for x,y in pos_spd:
            time.append(float(target-x)/y)
        n_fleet=0
        while time:
            temp1=time.pop()
            while time and time[-1]<=temp1:
                time.pop()
            n_fleet+=1
        return n_fleet