print(round(2.666666666666666, 2))

print(8 // 3) # This is called flow division resulting in 2 exluding the decimals

print(8 % 3) # This gives your only the remender expluding the divisor itself. Thus modulo division

score = 0
score += 1 # Thus an incrementer
score -= 1 # Thus a decrement


# TO overcome conversion during printing of data types we use F Strings
#####Example

score = 0
height = 1.8
isWinning = True

# Putting all these in a single print is worth using fStrings instead of converting all data to similar type

print(f"Your score is {score}, your heigh is {height} and you are winning is {isWinning}")