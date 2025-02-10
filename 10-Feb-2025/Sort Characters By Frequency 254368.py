# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
      dic = Counter(s)

      sorted_lst = sorted(dic.items(), key=lambda item: item[1], reverse=True)

      return "".join(char * freq for char, freq in sorted_lst)