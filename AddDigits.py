class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        st = str(num)
        stl = list(st)

        while len(stl) >1:
            temp = 0
            for i in stl:
                temp = temp + int(i)

            temps = str(temp)
            stl = list(temps)

        return int(stl[0])
