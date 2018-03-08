class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        st = list("{0:b}".format(num))
        st1 = []

        for i in st:
            if i == "0":
                st1.append("1")
            if i == "1":
                st1.append("0")

        res = "".join(st1)
        res = int(res, 2)
        return res



