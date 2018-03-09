class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = s.split(" ")
        st1 = ""
        for i in st:
            temp = list(i)
            temp.reverse()
            temp = "".join(temp)
            st1 = st1 + temp + " "

        st1 = st1[:-1]
        return st1
