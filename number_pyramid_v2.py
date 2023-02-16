#:)
#:):)
#:):):)
#:):):):)
#:):):):):)
#:):):):):):)
#:):):):):):):)
#:):):):):):):):)
#:):):):):):):):):)

#print the above using a for loop and a while loop.
#use print("\U0001f600") to print the smiley.

#i = 1

l = "\U0001f600"

for i in range(1,10): #this loop
	j = 1
	while j < i: #this loop adds smileys next to each other.
		print(l, end="")
		#print(j,l, end="") #use this to debug and understand the code.
		j = j + 1#this is to break out of this while loop.	
	print(l)	
	#print(i,l) use this to debug and understand the code.

#In each iteration of the inner loop, 
#the string "1" is printed to the console using the print() function with 
#the end parameter set to an empty string to prevent a newline character from being printed. 
#After the inner loop finishes, a newline character is printed to start the next line of the pattern.	

		
#I have to somehow contatenate \U0001f600 everytime I run through the loop.

