# 1

# 2 (2)
# 1 -> 1
# 2

# 3 (3)
# 1 -> 1 -> 1
# 1 -> 2
# 2 -> 1

# 4 (5)
# 1 -> 1 -> 1 -> 1
# 1 -> 1 -> 2
# 1 -> 2 -> 1
# 2 -> 1 -> 1
# 2 -> 2

# 5 (8)
# 1 -> 1 -> 1 -> 1 -> 1
# 1 -> 1 -> 1 -> 2
# 1 -> 1 -> 2 -> 1
# 1 -> 2 -> 1 -> 1
# 1 -> 2 -> 2
# 2 -> 1 -> 1 -> 1
# 2 -> 1 -> 2
# 2 -> 2 -> 1

# n 
# 1 
# ... (n - 1) patterns starting from 1
# 1 
# 2
# ... (n - 2) patterns starting from 2
# 2


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            answer = 0
            n1 = 1
            n2 = 2
            for i in range(3, n + 1):
                answer = n1 + n2
                n1 = n2
                n2 = answer
            return answer
                