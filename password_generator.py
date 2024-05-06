# **********Random password generator********

import random
import string
print("welcome to our random password")
def my_fun():

    length=int(input("enter the length:"))
    lowerD=string.ascii_lowercase
    upperD=string.ascii_uppercase
    digit= string.digits
    symbols=string.punctuation
    combine=lowerD+upperD+digit+symbols
    x=random.sample(combine, length)
    password=''.join(x)
    print("here is your new password",password)
    my_fun()

my_fun()


# ***********temperature converter**********
# unit= input("in this temperatue in celscius or fahrenheit(C\F):")
# temp= float(input("enter a temperature:"))
# if unit== "C":
#      temp=round((9*temp)/5 +32,1 )
#      print(f"temperature in fahrenheit is: {temp}^F")
# elif unit=="F":
#     temp=round((temp-32)*5/9 ,1 )
#     print(f"temperature in fahrenheit is: {temp}^C")
# else:
#     print("not found")      
     