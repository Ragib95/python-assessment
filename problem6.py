n = int(raw_input('Enter size of list: '))
arr = list()
for _ in xrange(n):
	arr.append(tuple(map(int, raw_input('Enter Tuple: ').split())))

print sorted(arr, key=lambda x:x[-1])