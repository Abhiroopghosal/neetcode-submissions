class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list1 = []
        
        groups = {}
        for i in strs :
            key = "".join(sorted(i))
            if key not in groups:
                groups[key] = []
            
            groups[key].append(i)

        return list(groups.values())