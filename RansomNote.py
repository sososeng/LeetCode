class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        st = list(ransomNote)
        res = True
        for i in st:
            if magazine.find(i) == -1:
                res = False
            else:
                magazine = magazine.replace(i,"",1)
        return res
