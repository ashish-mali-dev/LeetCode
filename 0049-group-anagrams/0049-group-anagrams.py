class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list) # Automatically initializes a missing key with an empty list

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        return list(anagram_map.values())

# Anagram words are just letters rearranged, when we sort them we get a unique key