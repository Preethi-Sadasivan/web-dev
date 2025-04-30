def squareperi(x):
  perimeter=4*x
  print("Perimeter of Square is",perimeter)

def rectangleperi(l,b):
  perimeter = 2*(l+b)
  return perimeter

def circumference(r):
  c=2*3.14*r
  print("Circumference of Circle is",c)

r=int(input("Enter radius of Circle:"))
circumference(r)

x=int(input("Enter side of square->"))
squareperi(x)

l = int(input("Enter length of rectangle->"))
b = int(input("Enter breadth of rectangle->"))
print("The Perimeter of Rectangle is " ,rectangleperi(l,b))