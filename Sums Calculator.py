#Author Joshua Bard 
#initialise the variables
sumTotal=0
sumEven=0
sumOdd=0

#inputs a number
input_number = int(input("Please insert a positive integer "))

#prints what that number is
#print("The integer you chose was ") +str(input_number)

#while loop
while (0<input_number):
    
    #if else to determine odds and even integers
    if(input_number % 2 == 0):
        sumEven = sumEven + input_number  
   
    else:
        sumOdd = sumOdd + input_number
    
    #adds to the total and substrats the input integer by -1    
    sumTotal = input_number + sumTotal
    input_number = input_number - 1
        
#prints the results of the integers
print("The sum of all even integers are " +str(sumEven))
print("The sum of all odd integers are " +str(sumOdd))
print("The sum of all integers are " +str(sumTotal))

#http://www.codeskulptor.org/#user44_8d7fkdwfky_0.py