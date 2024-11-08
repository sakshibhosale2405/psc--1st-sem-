# print ("Happy Diwali")
# number=int(input("enter a number: "))
# if number%4 == 0: 
#      print("yes")
# elif number%5==0:
#     print ("yes")  
# else:
#     print ("no")
# word="happy diwali"
# for _ in range(100):
#     print (word)
# i=0
# i+= 1
# for i in range(1,101):
#     print(i)
# i=1
# i+=1
# for i in range(1,21):
#     num =i*i
#     print(num)

# def fibonacci_numbers(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fibonacci_numbers(num-2)+fibonacci_numbers(num-1)
 
 
# n = 11
# for i in range(0, 11):
    # print(fibonacci_numbers(i), end=" ")
def fibonacci_numbers(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci_numbers(num-2)+fibonacci_numbers(num-1)
 
 
n = 200
for i in range(0, 200):
    print(fibonacci_numbers(i), end=" ")
      
      
      



    

