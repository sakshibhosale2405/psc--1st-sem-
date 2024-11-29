
# 1. Find 2nd big element from three numbers.
# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# c=int(input("enter a number:"))
# # 1. a<=b<=c:
# if a<=b and b<=c:
#     print(b)
# elif a<=c and c<=b:
#     print(c)
# elif b<=a and a<=c:
#     print(a)
# else:
#     print("invalid input")



# 2. Write a Python program to determine whether a given year is a leap year. A year is considered a leap year if it satisfies the following conditions:
# 	a) The year is evenly divisible by 4 and
# 	b) The year is not evenly divisible by 100, unless it is also evenly divisible by 400.
# (Generate two test cases that covers the above conditions).
# def leap_year(year): 
#     if year % 4 == 0 and (year % 100 != 0 or  year % 400 == 0):
#          return True
#     else:
#          return False
                
# print(leap_year(2024))




# 3)Write a function to find the sum of two numbers and return the sum.
# def sum (A,B):
#     print(A+B)

# sum(5,7)


# 4)Write a function that takes an integer input and checks whether it is a prime number or not
# def check_prime(num):
#     if num < 0:
#         print("enter a positive integer")
#     else:
#         if num>=1:
#          for i in range(2, num+1):
#           if (num % i) == 0:
#             print(num,"is a prime number")
#             break
#         else:
#             print(num,"is not a prime number")
# print(check_prime(7))

# 5. Write a function to count the sum of digits in a number.
# Ex: For example input 12305, output is 11.
# Explanation: 1+2+3+0+5 = 11
# def sum_of_digits(num):
#     return sum(int(digit) for digit in str(num))
# print(sum_of_digits(12305))


# 6. Write a function to check whether a number is a palindrome or not.
def is_palindrome(num):
    return str(num) == str(num)[::-1]
print(is_palindrome(12321))  

        
        


        
    
