# age=int(input("enter age"))
# if age<18 :
#     print("teenager")
# elif age>=18 and age<30:
#     print("adult")
# elif age>= 30:
#     print("senior")
# else:
#      print("enter a valid age")


        
# age1=int(input("enter age1:"))
# age2=int(input("enter age2:"))
# age3=int(input("enter age3:"))
# if   age1<18:
#     print("teenager")
# elif age1>=18 and age1<30:
#     print("adult")
# elif age1>=30 :
#     print("senior")
# if   age2<18:
#     print("teenager")
# elif age2>=18 and age2<30:
#     print("adult")
# elif age2>= 30 :
#     print("senior")
# if   age3<18:
#     print("teenager")
# elif age3>=18 and age3<30:
#     print("adult")
# elif age3>= 30 :
#     print("senior")

# sove question with use of function
def print_age_category(age):
    if age<18:
        print("teenage")
    elif 18<=age<30:
        print("adult")
    elif age>=30:
        print("senior") 
    else:
        print("enter a valid age")
    
age1=int(input("enter age1:"))
age2=int(input("enter age2:"))
age3=int(input("enter age3:"))   
print(print_age_category(age1))


       