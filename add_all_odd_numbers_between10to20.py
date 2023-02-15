# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0

for i in range(10, 20):
    if i % 2 != 0:
        x = x + i
print(x)

+++++++++++++++++++++++++++++++
#another way of doing it

for n in range(10, 21):  #remember range is exclusive, so we have to go up to 21
    if n % 2 != 0:
        x += n
print(x)        
+++++++++++++++++++++++++++++++
#Instead of looping over every number between 10 and 20, this solution only loops over the odd numbers.  
#Remember, the 3rd argument to range() is the STEP or interval that you want the range to increment by.

x = 0
 
for i in range(11,21,2):
        x += i
print(x)        
