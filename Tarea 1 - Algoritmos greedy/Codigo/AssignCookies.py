class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
 
        child = cookie = 0
        satisfied = 0
 
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                satisfied += 1
                child += 1
                cookie += 1
            else:
                cookie += 1
 
        return satisfied