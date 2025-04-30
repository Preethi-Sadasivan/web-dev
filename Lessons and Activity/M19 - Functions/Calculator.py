def add(P, Q):
   return P+Q

def subtract(P, Q):
  return P - Q

def multiply(P, Q):
  return P * Q

def divide(P, Q):
 return P / Q
# Now we will take inputs from the user
print("Please select operation.")
print("A. Add")
print("S. Subtract")
print("M. Multiply")
print("D. Divide")

choice = input("Please enter choice (A/S/M/D):")

num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))

if choice == 'A':
  print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == 'B':
  print(num_1, "-", num_2, "=", subtract(num_1, num_2))
elif choice == 'C':
  print(num_1, "*", num_2, "=", multiply(num_1, num_2))
elif choice == 'D':
  print(num_1, "/", num_2, "=", divide(num_1, num_2))
else:
  print("This is an invalid input")