def cube(num):
    return num ** 3

def is_divisible_by_3(num):
    if num % 3 == 0 :
        return cube(num)
    else:
         return "The number is Not divisible by 3"       



num = int(input("Enter a number: "))

print (is_divisible_by_3(num))