'''
Given a string s and an integer k, return the length of the longest substring that contains at most k distinct characters.

s = "eceba", k = 2
Output: 3
Explanation: The longest substring is "ece" which its length is 3.
'''

def returnSubstring(s: str, k: int):
    l = 0
    longest = 0
    setChars = set()
    n = len(s)

    for r in range(n):
        while len(setChars) > k:
            setChars.remove(s[l])
            l += 1
        
        w = (r - l) + 1
        longest = max(longest, w)
        setChars.add(s[r])
    
    return longest-1

print(returnSubstring("ecececba", 2))

# w = 1, longest = 1, setChars = {e}
# w = 2, longest = 2, setChars = {e, c}
# w = 3, longest = 3, setChars = {e, c}
# w = 4, longest = 4, setChars = {e, c, b}
# w - 5, 

