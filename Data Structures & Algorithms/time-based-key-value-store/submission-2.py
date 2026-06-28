class TimeMap:

    def __init__(self):
        self.tm={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tm:
            self.tm[key]=[]
        self.tm[key].append((timestamp,value))
        return None

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tm:
            return ""
        for keys,values in self.tm.items():
            if keys==key:
                l,r=0,len(values)-1
                while l<=r:
                    m=(l+r)//2
                    if values[m][0]==timestamp:
                        return values[m][1]
                    if values[m][0]>timestamp:
                        r=m-1
                    else:
                        l=m+1
                if values[l-1][0]<timestamp:
                    return values[l-1][1]
                else:
                    return ""
