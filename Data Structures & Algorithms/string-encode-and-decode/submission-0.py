class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for x in strs:
            encoded+="".join([str(len(x)),"*",x])
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        list_word=[]
        i=0
        l=""
        lnum=0
        word=""
        while i<len(s):
            if s[i]!="*":
                l+=s[i]
                i+=1
            else:
                lnum=int(l)
                word=s[i+1:i+lnum+1]
                i=i+lnum+1
                list_word.append(word)
                l=""
                lnum=0
                word=""
        return list_word