class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ttt = {}
        for lists in strs:
            key = ''.join(sorted(lists))
            # check if exists as a key
            if key in ttt.keys():
                ttt[key].append(lists)  
            else:  
                ttt[key] = [lists]
        return list(ttt.values())