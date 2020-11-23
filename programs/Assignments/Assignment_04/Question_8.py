# Developed By : Rishabh Gupta

# Question is-  Write a Python function to check whether a number is perfect or not.

# /*In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors,
# that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum).
# Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).
# Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6.
# Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6.
# The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128*/


a = eval(input("enter any no- "))

lst = []
for i in range(1, a+1):
    if(a%i == 0):
        lst.append(i)

sum_of_divisors_including_itself = sum(lst)

if (sum_of_divisors_including_itself // 2 == a):
    print("given number is the perfect number")
else:
    print("given number is not the perfect number")
