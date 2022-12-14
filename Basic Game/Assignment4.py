import simplegui
import time
import random

#-----------------------------------------------------------------------------------------------
#Global variables. Please do not change these!
WIDTH = 800
HEIGHT = 600
count=0
changeCount=0.0
position =[400,300]
velocity=[random.randrange(1,13),random.randrange(1,3)]
acceleration=[0,0]
timer=time.time()
sequence=[0,1,2,3,4] #default sequence of colors
sound_switch='N'
blink_speed =.3 #adjust this for faster or slower blinking of circles
start_game =False

#loads the splash screen
splash_screen ="https://www.dropbox.com/s/y5zes0s4fzlv2ku/play_button-512.png?dl=1"
splash_image=simplegui.load_image(splash_screen)
#-----------------------------------------------------------------------------------------------


"""
-----------------------------------------------------------------------------------------------
Q1 Enter the drop box links and make sure its shown in the canvas (3Marks)*
Insert your dropbox links here, make sure you set the "?dl=1" parameter like sample example below else your dropbox files wont load.
-----------------------------------------------------------------------------------------------
"""

ball_link="https://www.dropbox.com/s/ccb368b4fu8e1th/single-clipart-baloon-19.png?dl=1"
sound_link="https://www.dropbox.com/s/85up982vkph6z95/Robot_blip_2-Marianne_Gagnon-299056732.mp3?dl=1"
backgroundImage_link="https://www.dropbox.com/s/6hmh93emd7ky64y/football-field-quotes-quotesgram-14.png?dl=1"

#These functions below load your image and sound into the program
ball_image = simplegui.load_image(ball_link)
sound = simplegui.load_sound(sound_link)
background_image = simplegui.load_image(backgroundImage_link)

#You could control the sound of your music from below, enter values from 0.0 to 1.0, note the decimals
sound.set_volume(.5)




"""
------------------------------------------------------------------------------------------------------ 
#Qn2a This function should check if the ball has collided with the wall and reverse the direction of ball.
#This creates the effect of reflection/bouncing of the wall effect. The position of the ball is effected by
#the velocity parameter (x1,y1). if the ball collides with the left or right wall, we make the x1 component
#negative. If it collides with the top or bottom ball, the y1 component needs to be reversed.
#Movement of any object is defined as position x(t+1) = x(t) + x1(t) and y(t+1)=y(t) + y1(t), where x and y are
#postion of the ball on the canvas and x1 and y1 are its velocity components (4 Marks)***
#Qn2b
#This function also sets the switch to play sound. So when you detect a collusion
#set the sound_switch to 'Y' (1 Mark)
#Qn2c Increment the count by 1 in case of collision with the walls (1 Mark)
------------------------------------------------------------------------------------------------------ 
"""

def check_for_collision(position,velocity,sound_switch,count,radius=40):
    x1=velocity[0] # the horizonal velocity componenent
    y1=velocity[1] # the vertical velocity component
    sound_switch ='N'#Set this to Y if you think there has been a collusion
    impact_switch ='N'#Set this to Y if you think there has been a collusion, could use this to update count and sound
    #The above components should be modified if the ball has collided with the walls
    
    #========= Enter your code below =======================#

    
    #Check for left wall impact
    if position[0] <= 0:
        x1 = -x1
        sound_switch='Y'
        count+=1
        
        
    #check for right wall impact
    if position[0] >= WIDTH: 
        x1 = -x1
        sound_switch='Y'
        count+=1
    
    #check for top wall impact
    if position[1] <= 0:
        y1= -y1
        sound_switch='Y'
        count+=1
        
    #check for bottom wall impact
    if position[1]>= HEIGHT:
        y1= -y1
        sound_switch='Y'
        count+=1
        
    #set the sound_switch
    
    
    #update the count each time a collision occurs
    
    
    #===========================================================#
    
    #Do not change the two lines below
    velocity=[x1,y1]
    return velocity,sound_switch,count

#------------------------------------------------------------------------------------------------

"""
------------------------------------------------------------------------------------------------------ 
Q3 Color of the triangles on the screen can be changed based on time
your challenge here is to cycle the colors of the 4 circles on the screen. Each circle starts with
a different color and must change every 1 seconds in sequential order creating a special effect.
You need to select 5 colors of your choice from the website. https://htmlcolorcodes.com/
Each color has its own Hex code starting with #, for example black has a html code (#070707). You need to
select 4 colors of your choice from the options there and fill the below list. You can add more than 4 colors but
it won't be utilized in the program. No marks will be provided for default colors here.
------------------------------------------------------------------------------------------------------ 
"""

#========= Enter your code below =======================#
    
def rotate(color_list):
    color_list[-1] + color_list[0]

#change the below list with your color codes
color_list=['#1E8449','#1ABC9C','#99A3A4','#9B59B6']

for i in color_list:
    rotate(color_list)
    
#===========================================================#

"""
BONUS question with 2 additional marks! (Bonus Marks: 2)
"""
def change_color_every_1_second(sequence,timer,changeCount):
    global blink_speed
    #time here is in milliseconds, 100 milliseconds make a second. The timer starts running from the moment the
    #program starts. So you need to check for multiples of 100. You cannot use modulus operator why ?
    #ChangeCount variable counts how many times you have changed the sequence of colors of the circle since
    #the program started executing. So ideally if the time is currently 202 milli seconds, then you should have
    #changed the sequence twice by now. This means that you initiate a change only when timer exceeds the number 
    #of changes. For example 202/100 > changeCount, then you should change the sequence of colors.
    #remember to use float before comparison and also to update change count after changing color sequence
    
    #Hints: Check if time passed and sequence change are in sync. If it is don't do anything

        
    #If they are not in sync, change the sequence list.
    #the sequence list looks like [0,1,2,3,] meaning first circle will have 0th color corresponding to
    #0th color from your color_list and so on. After the first sequence shift, sequence list should look like
    #[3,0,1,2], next shift =[2,3,0,1] and so on. Make your code changes below.
   
    
    
    #increment the changeCount variable by 1 incase you have changed the sequence
    
    
    
    return sequence,changeCount
    

""" 
=============================================
Any modifications past this line are optional.
==============================================
"""

#The draw handler will draw the canvas refreshing it 60 times every second
def draw_handler(canvas):
    #This draws the boarder
    global velocity,sound_switch,count,position,timer,changeCount,sequence,start_game
    canvas.draw_polygon([(0, 0), (800, 0), (800, 600),(0, 600)], 12, 'Green')
    image_width=background_image.get_width()
    image_height=background_image.get_height()
    #format loaded image, centre of image, width and height of image, where you want the centre of image to be on canvas,
    #How much do you want it to be drawn( Ideally entire canvas.
    #If you are not sure of this, do not change these settings
    canvas.draw_image(background_image, (image_width/2, image_height/2),  (image_width, image_height), (WIDTH/2, HEIGHT/2),(WIDTH, HEIGHT))
    ball_width=ball_image.get_width()
    ball_height=ball_image.get_height()
    
    if start_game:
    #Call the function to check for collusions
        velocity,sound_switch,count=check_for_collision(position,velocity,sound_switch,count,radius=30)
    #Call the function to update colors of the circles
        sequence,changeCount=change_color_every_1_second(sequence,time.time()-timer,changeCount)
        position[0]=position[0]+velocity[0]
        position[1]=position[1]+velocity[1]       
        
    
    #play sound in case of collusion
    if sound_switch =='Y':
        sound_switch='N'
        sound.rewind()
        sound.play()

    
    #Draw the count text here
    
    canvas.draw_text(str(count), (700, 50), 30, 'white', 'serif')
    
    #Draw the custom ball
    canvas.draw_image(ball_image, (ball_width/2, ball_height/2),  (ball_width, ball_height), position,(30,30))
    
    

    #In case you want to be more creative, you could change the position of the circle on the screen
    #you can play around with the positon of the circles. (400,250) specifies the position
    #remember the whole canvas is 800,600 and it should be within these boundaries
    #canvas.draw_circle((x,y), radius,line width, line color, fill color)
    
    
    
    canvas.draw_circle((400,100), 20, 1, 'Black', color_list[sequence[0]])
    canvas.draw_circle((400,200), 20, 1, 'black', color_list[sequence[1]])
    canvas.draw_circle((400,400), 20, 1, 'black', color_list[sequence[2]])
    canvas.draw_circle((400,500), 20, 1, 'black', color_list[sequence[3]])
    
    #Display the play/resume splash screen
    if not start_game:
        splash_width=splash_image.get_width()
        splash_height=splash_image.get_height()
        canvas.draw_image(splash_image, (splash_width/2, splash_height/2),  (splash_width, splash_height), (250, 120),(150,150))
        canvas.draw_text("HIT SPACE TO", (220, 180), 10, 'orange', 'serif')
        canvas.draw_text("START", (240, 190), 10, 'orange', 'serif')
    
def key_handler(key): 
    global start_game
    if start_game:
        start_game= False
    else:
        start_game= True
        
        


#Create a simple frame
frame = simplegui.create_frame('Bouncing balls', WIDTH, HEIGHT)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(key_handler)
frame.start()
