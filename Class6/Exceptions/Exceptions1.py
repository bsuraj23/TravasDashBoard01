# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Division by zero error line 4")

   
def add():
    
        a = int(input("Enter first number"))
        b = int(input("Enter second number"))
        print("Addition is ", a + b)    
    






# a=90
try:
    a=90
    b= int(input("enter b value  "))
    c=a/b
    print("Result is ",c)

except ValueError:
    print("Invalid input, please enter a valid number. Please take care")
except ZeroDivisionError:
    print("Division by zero error this is my msg ")
finally:
     print("Execution completed")
