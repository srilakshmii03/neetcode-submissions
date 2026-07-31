class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        c_to_w , w_to_c = {}, {}
        for i in range(len(pattern)):
            char, word = pattern[i], words[i]
            if char in c_to_w:
                if c_to_w[char] != word:
                    return False
            else:
                c_to_w[char] = word
            if word in w_to_c:
                if w_to_c[word] != char:
                    return False
            else:
                w_to_c[word] = char
        return True
