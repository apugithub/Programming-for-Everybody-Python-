## Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message 
##and ignore the number. Enter the numbers from the book for problem 5.1 and Match the desired output as shown.

largest=None
smallest= None
while True:
    inp= raw_input('Enter the number: ')
    if inp== 'done':
        break
    if len(inp)<1 : 
        break
    try:
        num= float(inp)
    except:
        print ("Invalid input")
        continue
    
    if largest is None and smallest is None:
        
        largest=num
        smallest=num
    elif num>largest :
        largest=num
    elif num<smallest :
        smallest=num
            
print ("Maximum is"), int(largest)
print ("Minimum is"), int(smallest)
