import turtle

turtle.Screen().bgcolor("orange")   

sc = turtle.Screen()

sc.setup(300,400)

turtle.title("Welcome to Turtle Window")

board = turtle.Turtle() #defined variable

for i in range(4): #iterate loop for total number of side   
        board.forward(100) #forward movement of turtle
        board.left(90) 
        i = i +1 
        
turtle.done()