from Week2.Test import TestFunctional

l1 = TestFunctional()  # reference of Test_LinkedList class


class Prime_2D:
    try:
        num = 1000
        l1.prime_number1(num)  # calling function
    except RuntimeError:     # handling exception
        print("oops something went wrong...\n")
