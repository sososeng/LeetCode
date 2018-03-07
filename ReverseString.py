class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = list(s)
        st.reverse()
        st = "".join(st)
        return st
