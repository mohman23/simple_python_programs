# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0

# YOUR CODE GOES HERE:
for i in range(10, 20):
    if i % 2 != 0:
        x = x + i
print(x)
