def getemployeedetails():
  return(input("Enter the name of the employee: "), int(input("Enter the experience of the employee: ")))    

def salary(exp):
  if exp>=5:
    return 3000000
  elif exp>=3:
    return 1000000
  else:
    return 500000
  

name,experience = getemployeedetails()

emp_salary= salary(experience)
print("The salary of " , name , "is", emp_salary)