class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}
        for a, b in zip(s, t):
        #     if(a in countS):
        #         countS[a] +=1
        #     else:
        #         countS[a]=1
        #     if(b in countT):
        #         countT[b] += 1
        #     else:
        #         countT[b]=1
        # print(countS, countT)
            countS[a] = countS.get(a, 0) + 1
            countT[b] = countT.get(b, 0) + 1
        return countS == countT