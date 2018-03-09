class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        st = str(x)

        if x < 0:
            st = st[1:]
            st = list(st)
            st.reverse()
            st = "".join(st)
            st = "-"+st
        else:
            st = list(st)
            st.reverse()
            st = "".join(st)

        st = int(st)

        if st > 2147483647:
            st = 0

        if st < -2147483647:
            st = 0
        return int(st)
