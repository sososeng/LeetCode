class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        JS = list(J)
        SS = list(S)
        res = 0
        for i in range(0,len(JS)):
            for j in range(0,len(SS)):
                if JS[i] ==SS[j]:
                    res = res +1

        return res
