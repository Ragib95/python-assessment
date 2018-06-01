import collections

file = (open('input.txt').read()).split()
frequency = collections.Counter(file)

f = open("output.txt","a")
for i in sorted(frequency):
	f.write(i + ' : ' + str(frequency[i]) + '\n')