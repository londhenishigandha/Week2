
from Week2.util import Test_LinkedList
l1 = Test_LinkedList()


class Balanced_Parentheses:
    while True:
        try:
            print("enter a parentheses expression..\n")
            string = str(input())

            if string.isdigit() is True or string.isalpha() is True:
                print("enter valid input...\n")
            elif string.isidentifier() is True:
                print("enter valid input...\n")
            else:
                l1.balanced_parentheses1(string)

            break
        except ValueError:
            print("please enter valid input..\n")
            continue
        except RuntimeError:
            print("oops something went wrong..\n")
            continue
