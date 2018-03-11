class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        st = list(s)

        if len(st) == 1:
            return 0

        for i in range(0, len(st)):
            check = True
            for j in range(0, len(st)):
                if st[i] == st[j] and i != j:
                    check = False

            if check:
                return i

        return -1