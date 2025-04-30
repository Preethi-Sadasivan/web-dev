def add(P, Q):
   return P+Q

def subtract(P, Q):
  return P - Q


print("Please select operation.")
print("A. Add")
print("S. Subtract")

choice = input("Please enter choice (A/S):")

num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))

if choice == 'A':
  print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == 'B':
  print(num_1, "-", num_2, "=", subtract(num_1, num_2))