for i in [1,3,5,7,9]:
    print(i)


#making it more dynamic
oddNumbers=[1,3,5,7,9]

#print even numbers
for i in oddNumbers:
    print(i*2)

# Now applying range


for i in range(9):
    print(i)
    #This prints 0 to 8 excluding 9 

# If you want 1 to 9 then
print("start here", end="\n")
for i in range(1,10):
    print(i, end=" ")

#So incase you want the same output of odd number 1 to 9
#In the range you give it three values
# a The starting values
#b the range where it should stop
#c the the position it will skip

print("\n\nStart here from the above explanation")
for i in range(1,10,2):
    print(i, end=" ")

#Code challenge the for loop that prints out all the even numbers from 1 to 19
print("\n\nEven numbers from 1 to 19")
for i in range(2,20,2):
    print(i, end=" ")
#Something important to note is that is usually begins with the a in the range while printing.    

#printing all integers between -2 and 5
print("\n")
for i in range(-1,5):
    
    print(i, end=",") 

    
#In short it's on incremental basis for range(a,b,c)
#on printing its incremental thus a, a+c, result+c untill before b because b is not printed   

print("\n\n\n")
for i in range(1,10,4):
    print(i, end=(","))     

#In conclusion if the value is range(1,10) thier is a default increment of a 1    