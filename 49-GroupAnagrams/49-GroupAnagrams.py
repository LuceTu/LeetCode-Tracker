# Last updated: 10/26/2025, 4:57:15 PM
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)           # key: 频次数组tuple, value: 同组单词列表

        for word in strs:                    # ① 遍历单词
            count = [0] * 26
            for ch in word:                  # ② 遍历字符
                count[ord(ch) - ord('a')] += 1
            key = tuple(count)               # ③ 频次数组必须在内层循环结束后再转成key
            groups[key].append(word)         # ④ 追加的是原始单词
        return list(groups.values())    