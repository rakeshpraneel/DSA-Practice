'''
Write a short program that prints each number from 1 to 100 on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''


def process():
    dict_ ={
        3: ""
    }
    for i in range(1,101):
        '''
        i%key == 0 and i/key in key()
        i=i/key
        i%key
        '''
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)

# process()


def process2(num):
    '''
    Write an algorithm to determine if a number n is happy.

    A happy number is a number defined by the following process:

        Starting with any positive integer, replace the number by the sum of the squares of its digits.

        Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.

        Those numbers for which this process ends in 1 are happy.

        Return true if n is a happy number, and false if not.

    7 -> 49 -> 97 -> 130 -> 10 -> 1

    2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4

    49%10 = 9


    :return:
    '''

    flag = True
    visited = []
    sum_ = 0

    def recc(num):
        sum_ += int(num%10)*int(num%10)
        num = int(num / 10)
        if sum_ in visited:
            # flag = False
            return "Not Happy"
        if sum_ == 1:
            # flag = False
            return "Happy"
        visited.append(sum_)
        num = sum_
        sum_ = 0

    recc(num)

    while flag:
        print(num)
        while num > 0:
            sum_ += int(num%10)*int(num%10)
            num = int(num / 10)
        if sum_ in visited:
            # flag = False
            return "Not Happy"
        if sum_ == 1:
            # flag = False
            return "Happy"
        visited.append(sum_)
        num = sum_
        sum_ = 0

print(process2(2))

