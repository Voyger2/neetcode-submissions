class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final=[]
        visited = [False]*len(strs)
        for i in range(len(strs)):
            if visited[i] == True:
                continue
            current = [strs[i]]
            for j in range(i+1,len(strs)):
                x = sorted(strs[i])
                y = sorted(strs[j])
                if visited[j] == True:
                    continue
                if x==y:
                    current.append(strs[j])
                    visited[j] = True
            final.append(current)
        return final