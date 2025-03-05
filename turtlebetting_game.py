# here Iam importing all the modules needed

import turtle  
import time
import random

color_of_pieces=['red','green','yellow','blue']

wn = turtle.Screen()

pieces=[]
# creating all the four pieces needed to participate in the game abd defining their character
for i in color_of_pieces:
    t=turtle.Turtle()
    t.shape("turtle")
    t.color(i)
    pieces.append(t)


num=330
finsh=300
# function needed to draw the finish line 
def set_finishLine():
        drawer= turtle.Turtle()
        drawer.color("black")
        drawer.penup()
        drawer.forward(finsh)
        drawer.pendown()
        drawer.left(90)
        drawer.forward(400)
set_finishLine()        

# moving all thr cing turtles to starting point  
for j in pieces: 
       
         j.penup ()
         j.forward(-265)

         j.left(90)
         j.forward(num)
         j.right(90)
         num-=100 

time.sleep(2)   
# taking users bet on the terminal 
    
wn._root.withdraw()  
user_bet=input("enter your bet: ")
wn._root.deiconify()

random_numbers=random.sample(range(50,101),4)

# code that makes the turtles run at random distace at given period of time 
race_on=True
while race_on:
 for i in  pieces:
        

        i.forward(random.randint(1,10))
        if i.xcor()>=finsh:
                winner=i.color()[0]
                wn.bye()
                print(f"the winner of the race is {winner}")
                race_on=False
                break   
# declaring the winner and status of the user         
if winner==user_bet.lower():
        print("congratulation you win ")
else: 
                print("you lose")        
 


wn.mainloop()