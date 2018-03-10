class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        one = "qwertyuiop"
        two = "asdfghjkl"
        three = "zxcvbnm"
        res = []
        for i in words:

            checkone = True
            checktwo = True
            checkthree = True

            for j in list(i):

                if one.find(j.lower()) == -1:
                    checkone = False

                if two.find(j.lower()) == -1:
                    checktwo = False

                if three.find(j.lower()) == -1:
                    checkthree = False

            if checkone:
                res.append(i)
            if checktwo:
                res.append(i)
            if checkthree:
                res.append(i)

        return res