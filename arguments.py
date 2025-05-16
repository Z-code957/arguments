'''
1. Tip, the waiter
Outline:
Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant
. Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), this function calculates the total
 amount you should pay.

def total_bill(bill,tip):
    total=bill*(1+0.01*tip)
   # total=round(total,2)
    print(f"Please pay ${total}")
total_bill(2000,10)'''

'''
Cube of the cube
Outline:
Define a function to find a cube
 and define another function which let execute the cube function if the number is divisible by 3
'''
def cube(number):
    return number*number*number
print(cube(5))
def check(a):
    if a%3==0:
        return True 
    else:
        return False
print(check(330))