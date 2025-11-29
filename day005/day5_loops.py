########### FOR LOOPS ###################
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over a string
for char in "Python":
    print(char)

# Iterating using range()
for i in range(5):  # Iterates from 0 to 4
    print(i)


############ WHILE LOOP #####################
count = 0
while count < 5:
    print(count)
    count += 1



########### CONTROL FLOW STATEMENTS WITHIN LOOPS #############
# break: Terminates the loop immediately and transfers control to
# the statement following the loop.
#
# continue: Skips the rest of the current iteration and proceeds to
# the next iteration of the loop.
#
# else (with for and while loops): An optional else block can be
# added to both for and while loops. This block executes only if the
# loop completes normally (i.e., without encountering a break statement).

# Example with break
for i in range(10):
    if i == 5:
        break
    print(i)

# Example with continue
for i in range(5):
    if i == 2:
        continue
    print(i)

# Example with else
for i in range(3):
    print(i)
else:
    print("Loop finished normally.")