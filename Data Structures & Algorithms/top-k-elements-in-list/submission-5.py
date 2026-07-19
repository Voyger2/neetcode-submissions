class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        freq_list = []
        final = []
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        for numb, freq in seen.items():
            freq_list.append([freq,numb])
        freq_list.sort()
        for i in range(1,k+1):
            item = freq_list[-i]
            final.append(item[1])
        return final


        