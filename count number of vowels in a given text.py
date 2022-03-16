#You need to make a program that counts the number of vowels in a given text.
#The vowels are a, e, i, o, and u.

#Take a string as input and output the number of vowels.

#Sample Input:
#    this is great

#Sample Output:
#     4


x = input()
count = 0
for c  in x:
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        count += 1
print(count)
