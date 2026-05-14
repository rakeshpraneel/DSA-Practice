'''
Count Primes:
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
'''


class Solution:
    '''
    Runtime
1927
ms
Beats
26.49%

Memory
57.90
MB
Beats
91.39%

    '''
    # import math
    def countPrimes(self, n: int) -> int:
        # Logic is considering all the numbers first as prime
        # then iterate through every true number and makr its multiples as non prime
        prime = [True]*n
        if n <= 2:
            return 0
        for i in range(2,len(prime)):
            if prime[i]:
                for multiples in range(i*i,n,i):
                    prime[multiples] = False
        return prime.count(True)-2


# class Solution:
#     import math
#     def countPrimes(self, n: int) -> int:
#         c=0
#         while(n>1):
#             non_prime = True
#             for i in range(1,int(math.sqrt(n))+1):
#                 # print(i)
#                 if n%i == 0 and i!=1:
#                     non_prime = False
#                     break
#             if non_prime:
#                 # print(n)
#                 c+=1
#             n-=1
#         return c