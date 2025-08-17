class Solution(object):
 def lengthOfLastWord(self,s):
  s=s.rstrip()
  last_space=s.rfind(' ')

  return len(s) -last_space -1 
        