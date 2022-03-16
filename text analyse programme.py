#You are making a program to analyze text.
#Take the text as the first input and a letter as the second input, and output the frequency of that letter in the text as a whole percentage.

#Sample Input:
#hello
#l

#Sample Output:
#40

#The letter l appears 2 times in the text hello, which has 5 letters. So, the frequency would be (2/5)*100 = 40.
#Division result is a float. Use the int() function to convert the result to an integer.

text = input()
letter = input()
leen = len(text)
count = 0
for text in text:
    if letter in text:
        count += 1
per = (count/leen)*100
per = int(per)
print(per)
