class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        lookup1={}
        lookup2={}
        max_list=[float('inf'),-1,-1]
        for ch in t:
            lookup1[ch]=lookup1.get(ch,0)+1
        i,j=0,0
        have,need=0,len(lookup1)
        while j<len(s):
            lookup2[s[j]]=lookup2.get(s[j],0)+1
            if s[j] in lookup1 and lookup1[s[j]]==lookup2[s[j]]:
                have+=1
            while have==need:
                if (j-i+1)<max_list[0]:
                    max_list[0]=j-i+1
                    max_list[1]=i
                    max_list[2]=j
                lookup2[s[i]]-=1
                if s[i] in lookup1 and lookup1[s[i]]>lookup2[s[i]]:
                    have-=1
                i+=1
            j+=1
        if max_list[0]==float('inf'):
            return ""
        else:
            return s[max_list[1]:max_list[2]+1]
                
