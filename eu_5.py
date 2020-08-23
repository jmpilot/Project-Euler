'''Smallest positive integer that is evenly divisible by the numbers 1-20'''




def ed_2():

	x = 2
	y = 380

	while x<20:

		if y % x == 0:
			x += 1
			continue
		else:
			y = y + 380
			x = 2

	else:
		return y

print(ed_2())




