class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # modulo operation can be heavy as compared to addition, so kept track of next 3,5 and 15 and constructed answer.
        next3 = 3
        next5 = 5
        next15 = 15
        res = list()
        for i in range(1, n+1):
            if i == next15:
                res.append("FizzBuzz")
                next15 += 15
                next3 += 3
                next5 += 5
            elif  i == next3:
                res.append("Fizz")
                next3 += 3
            elif i == next5:
                res.append("Buzz")
                next5 += 5
            else:
                res.append(str(i))
        return res
