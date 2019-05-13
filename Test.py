
import numpy as np


class TestFunctional:

    """ ====  Leap Year checking  ====="""

    @staticmethod
    def leapyear(year):  # it is a static function which accepts input int (year)
        res = True
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  # checking the leap year condition
            print(str(year) + " it is  a leap year")
            res = True
        else:  # printing the result given input is leap year or not
            print(str(year) + " it is not a leap year")
            res = False


    """ ====  two-dimensional array concepts  ====="""

    @staticmethod
    def two_dimensional_array(m, n):  # it is a static method which accepts int values m(rows),n(columns)
        arr = [[0 for i in range(m)] for j in range(n)]  # arr with m rows and n columns
        for i in range(m):  # for i from m row
            for j in range(n):  # for j from n cols
                arr[i][j] = int(input("enter array element.."))  # reading user input and storing to the array
        array = np.array(arr)  # numpy is used for multidimensional arrays
        print(array)  # printing the array elements

        """ =========anagram problem =========="""

    @staticmethod
    def anagram(str1, str2):  # it is a static method which accepts two String as str1,str2
        if sorted(str1) == sorted(str2):  # sorting of str1 and str2 are equals it is anagram else not
            print("given strings are anagram \n ")  # if condition true print anagram
        else:
            print("given strings are not anagram \n ")  # else print not a anagram

        """ ========== prime numbers ==========="""

    @staticmethod
    def is_prime(start, end):  # it is a static method which accepts 2 int as parameter start and end parameter

        for val in range(start, end):  # taking user inputs from range start to end
            if val > 1:  # if val is greater than 1 moves to inner loop
                for n in range(2, val):  # range stars from 2 up to val
                    if (val % n) == 0:  # val % n == 0,then it is not a prime numbers
                        break  # exits from a program
                else:
                    print("prime values of given number is:", val)  # prints prime numbers for given range



        """ =======================  prime numbers of anagram  ======================="""

    @staticmethod
    def prime_number(n):
        my_list = []
        pm_list = []
        for i in range(0, n):
            if i > 1:
                result = True
                for j in range(2, i):
                    if i % j == 0:
                        result = False
                        break
                if result:
                    pm_list.append(i)
                    my_list.append(str(i))   # use here my_list.append(str(i))
        print("===prime numbers range n  are as follows......\n")
        print("prime numbers are:", pm_list)
        return my_list
        # return pm_list
    """============ code used for the printing 2D-prime Numbers=========="""
    @staticmethod
    def prime_number1(n):
        my_list = []
        pm_list = []
        for i in range(0, n):
            if i > 1:
                result = True
                for j in range(2, i):
                    if i % j == 0:
                        result = False
                        break
                if result:
                    pm_list.append(i)
                    my_list.append(str(i))   # use here my_list.append(str(i))
   
        print("prime numbers are:", pm_list)
        # return my_list
        return pm_list

    @staticmethod
    def anagram_prime(my_list):
        my_list1 = list()
        result = False
        size = len(my_list)
        for i in range(size):
            for j in range(i + 1, size):
                if sorted(my_list[i]) == sorted(my_list[j]):
                    my_list1.append(int(my_list[i]))
                    result = True
        ang_list = list()
        if result:
            print("=====list of anagram prime numbers are:====")
            for i in range(len(my_list1)):
                ang_list.append(int(my_list1[i]))
        print(ang_list)
        return ang_list

    @staticmethod
    def palindrome(n):
        rev = 0
        temp = n
        while n > 0:
            rem = n % 10
            rev = rev * 10 + rem
            n = n // 10
        if rev == temp:
            return temp


t = TestFunctional()  # creating reference of TestFunctional
