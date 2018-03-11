class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        st=[]
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                st.append("FizzBuzz")

            elif i % 3 == 0 and i % 5 != 0:
                st.append("Fizz")

            elif i % 3 != 0 and i % 5 == 0:
                st.append("Buzz")
            else:
                st.append(str(i))
        return st