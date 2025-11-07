#################### LOOPS ###########
# used for repetion of task or activities you wish to run a couple of times
# There are a couple of Loops including for loops, while loops , nested loops


############### Lets start off with "FOR LOOPS" ################
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")

    print(fruits) # This line causes the list to be printer at any loop instance cos it is in
                  #indented within the loop
print(fruits)     # This line causes the list to be printed once as it sits outside the loop