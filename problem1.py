
def special(passwd, n):
	for i in passwd:
		if i in ['$', '#', '@']:
			return True
	return False


def number(passwd,n):
	for i in passwd:
		if ord(i) in range(48,58):
			return True
	return False

def upperchar(passwd,n):
	for i in passwd:
		if ord(i) in range(65,91):
			return True
	return False

def lowwerchar(passwd,n):
	for i in passwd:
		if ord(i) in range(97,123):
			return True
	return False


def validate(passwd):
	n = len(passwd)
	if n < 6 or n > 12:
		return False
	if upperchar(passwd,n) == False:
		return False
	if number(passwd,n) == False:
		return False
	if lowwerchar(passwd,n) == False:
		return False


	return True


print 'Enter passwd'
passwd = raw_input()
if validate(passwd):
	print 'valid'
else:
	print 'not valid'