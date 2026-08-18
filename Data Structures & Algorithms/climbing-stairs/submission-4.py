class Solution:
    def climbStairs(self, n: int) -> int:
        #integer n -> num stps til goal
        # climb 1 or 2 stps
        #return number of distinct ways to climb to top
        if n == 1:
            return 1
        if n == 2:
            return 2
        else :
            one = 1
            two = 2
            for i in range(2, n):
                temp = two 
                two = one + two
                one = temp
            return two