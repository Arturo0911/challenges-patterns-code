#!/usr/bin/python3

class Solution:
    def longestPalindrome(self, s: str) -> str:
        memory = ''
        for x in range(len(s)):
            for y in range(len(s), x, -1):
                if len(memory) >= y-x:
                    break
                elif s[x:y] == s[x:y][::-1]:
                    memory = s[x:y]
                    break
        return memory
            
    


if __name__ == "__main__":
    print(Solution().longestPalindrome("babad"))
    print(Solution().longestPalindrome("cbbd"))
    # print(Solution().longestPalindrome("cbbd"))
    # print(Solution().longestPalindrome("babad"))
    # Solution().longestPalindrome("cbbd")
