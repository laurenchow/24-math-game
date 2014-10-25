import random

# feature list:
# need to check and see if all numbers entered are in the list of acceptable numbers
# need to control how users input numbers so that if they don't space the right away it still works
# need to have an option to keep playing so use while loop
# need to figure out a way to generate solvable sets of 24

ops, nums = [], []
solvable = {1 : (5, 6, 1, 2), 2 : (8, 11, 8, 1), 3: (6, 2, 2, 1), 
	4: (10, 4, 2, 12), 5: (2, 12, 5, 10)}

def challenge_numbers():

	rando = random.randint(1, 5)

	print "Here are your numbers:"
	random_problem = solvable[rando]
	print random_problem


def player_input():
	print "Make 24 using any combination of +-/*. You may only use each number once." 
	print "Also you have to use reverse Polish notation because I said so."
	
	print "Now please put in the four numbers, followed by your operations"
	print "followed by a return. Use a space between each."

	guess = raw_input()
	guess.rstrip()
	guess_list=guess.split(' ')

	for count in range(0, 4):
		nums.append(guess_list[count])

	for count in range(4,7):
		ops.append(guess_list[count])

	return ops, nums

def math_time(ops, nums):

	keep_playing = True

	while keep_playing == True:
		
		new_num = 0	

		if ops[0] == '+':
			new_num = int(nums[0]) + int(nums[1])	
		elif ops[0] == '-':
		 	new_num = int(nums[0]) - int(nums[1])
		elif ops[0] == '/':
			new_num = float(nums[0])/int(nums[1])
		elif ops[0] == '*':
			new_num = int(nums[0])*int(nums[1])
		else:
		 	print "Are you sure you put the right numbers in?"
		#  	# you should break the game if this happens and make a while loop 

		# print "After first operation, your new number is: %s" % new_num

		if ops[1] == '+':
			new_num = new_num + int(nums[2])
		elif ops[1] == '-':
		 	new_num = new_num - int(nums[2])
		elif ops[1] == '/':
			new_num = float(new_num)/int(nums[2])
		elif ops[1] == '*':
			new_num = new_num*int(nums[2])
		else:
		 	print "Are you sure you put the right numbers in?"
		
		# print "After second operation, your new number is: %s" % new_num

		if ops[2] == '+':
			new_num = new_num + int(nums[3])	
		elif ops[2] == '-':
		 	new_num = new_num - int(nums[3])
		elif ops[2] == '/':
			new_num = float(new_num) / int(nums[3])
		elif ops[2] == '*':
			new_num = int(new_num) * int(nums[3])
		else:
		 	print "Are you sure you put the right numbers in?"
		
		# print "After last operation, your new number is: %s" % new_num

		print "Your result is %r" % new_num
		if new_num == 24:
			print "You win!"
			break
		else:
			print "You lose!"

def play_again():
	answer = raw_input("Do you want to play again? Y/N")
	if answer == 'Y':
		challenge_numbers()
	else: 
		print "Goodbye!"

def main():
	challenge_numbers()
	player_input()
	math_time(ops, nums)
	play_again()

if __name__ == "__main__":
	main()