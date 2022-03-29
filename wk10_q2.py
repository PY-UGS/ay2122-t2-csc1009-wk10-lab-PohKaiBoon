def avg(input_X, input_Y): # function to calculate average
    return ((input_X+input_Y)/2)

input_X = int(input("Enter number X: ")) #input will be casted to int as input() always return a string
input_Y = int(input("Enter number Y: ")) #input will be casted to int as input() always return a string

print ("Average of X & Y: ",avg(input_X, input_Y))

