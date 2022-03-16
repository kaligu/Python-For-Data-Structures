#Take a string as input and output each letter of the string on a new line, repeated N times, where N is the position of the letter in the string.

#Sample Input:
#   data

#Sample Output:
#   d
#   aa
#   ttt
#   aaaa
#Hint: Use a loop to iterate over the string, keeping the position number of the current iteration in a variable. Then use multiplication to repeat the letters.

x = input()
count = 0
for c in x:
    count += 1
    print(c*count)
