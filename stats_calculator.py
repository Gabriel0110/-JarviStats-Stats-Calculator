#### PERSONAL NOTES ####
# Prompt for calculation
# When user specifies letter of calculation, let the user see the equation they selected, then continue to prompt for specific variables needed for that calculation
# When user defines all necessary variables needed, calculate the result

# 1. Create prompt of all calculations that you want
# 2. Implement all corresponding equations into the program for each calculation choice (separate functions)
# 3. Display the equation for the desired calculation so the user can see what variables are being used for that equation.
# 3. Implement the variable input system after user prompts for desired calculation. (i.e. "please provide data for the following variables, in order respectively: X, P, n, N, m..."

import time
import equations as eq

# INTRO
print("Nice to see you Gabe, my name is JarvStats! I can help compute "
+ "some statistical calculations for you!\n")

# PAUSE TO MAKE SEEM MORE AI-LIKE
time.sleep(2.5)

while True:

	# PROMPT FOR USER SELECTION, GIVING OPTIONS TO THE USER
	prompt = ("Please select a calculation for me to compute by " + 
	"choosing the letter for the corresponding calculation:\n ")
	
	prompt += ("\nA. Combination\nB. Permutation\nC. Binomial Dist.\n" + 
	"D. Negative Binomial Dist.\nE. Geometric Binomial Dist.\n...\n")

	choice = input(prompt)

	# CONDITIONAL FOR THE CHOICES
	if choice == "quit" or choice == "q": # Easy exit command
		break
	elif choice == "A" or choice == "a":
		print("\nYou chose Combination: nCr\n")
		time.sleep(1)
		print("The answer is " + str(eq.comb()) + "\n")
	elif choice == "B" or choice == "b":
		print("\nYou chose Permutation: nPr\n")
		time.sleep(1)
		print("The answer is " + str(eq.perm()) + "\n")
	elif choice == "C" or choice == "c":
		print("\nYou chose Binomial Distribution: (nCx)(p^x)(1-p)^n-x\n")
		time.sleep(1)
		print("The answer is " + str(eq.binDist()) + "\n")
	elif choice == "D" or choice == "d":
		print("\nYou chose Negative Binomial Distribution: " + 
		"(z-1 C r-1)(p^r)(1-p)^z-r\n")
		time.sleep(1)
		print("\nThe answer is " + str(eq.negBin()) + "\n")
	else: # If incorrect input, inform user and reset
		print("\nPlease make sure you used the correct input! Unfortunately, " +
		 "I am only a calculator right now, so I can only do specific things!\n")
		
time.sleep(1.5)		
print("\nGoodbye for now! Go study!")
