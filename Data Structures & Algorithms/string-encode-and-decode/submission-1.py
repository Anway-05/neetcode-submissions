class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list=[]
        for x in strs:
            encoded_list.append(f"{len(x)}*{x}")
        print(encoded_list)
        return "".join(encoded_list)

    def decode(self, s: str) -> List[str]:
        list_word=[]
        i=0
        lnum=0
        while i<len(s):
            if s[i]!="*":
                lnum=lnum*10+int(s[i])
                i+=1
            else:
                list_word.append(s[i+1:i+lnum+1])
                i=i+lnum+1
                lnum=0
        return list_word