num = int(raw_input())

while num != 1:
	print num,
	if num%2 == 0:
		num = num/2

	elif num%2 == 1:
		num = num*3 + 1

print 1
