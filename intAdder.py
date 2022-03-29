#Loop to enable handling of incorrect input
while True:
    try:
        print("Number adder")
        #Input and validation
        intInput = int(input("Please enter your number: "))
        print (intInput)
        #Convert int to string so that each character can be individually mapped to a list, and then convert back to int
        output = list(map(int, str(intInput)))
        #Each element of list is added and outputted
        print(sum(output))
    #Error handling
    except ValueError:
        print("Please enter a single integer")
    else:
        break
 



