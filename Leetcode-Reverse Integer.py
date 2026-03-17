import math
class Solution:
    '''
    Runtime 47ms Beats 50.99%
    Memory  19.42MB Beats 6.96%
    '''
    def reverse(self, x: int) -> int:
        limit = math.pow(2,31)
        print(limit)
        # l_limit = limit * -1
        # print(l_limit)
        ini = x
        final = 0
        x = x*-1 if x<0 else x
        while x > 0:
            # print(x%10)
            final = (final*10) + x%10
            # print(final)
            # print("--"*10)
            x = int(x/10)
            # print(x)
        if ini > 0 and final < limit:
            return final
        elif ini < 0 and final < limit:
            return final*-1
        else:
            return 0