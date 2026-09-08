class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            sort_str = tuple(sorted(string))  # convert to tuple
            print(sort_str)
            if sort_str not in anagrams:
                anagrams[sort_str] = []
            anagrams[sort_str].append(string)
        return list(anagrams.values())