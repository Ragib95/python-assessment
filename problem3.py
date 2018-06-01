def binarysearch(arr, num):
	end = len(arr) -1
	start = 0
	while start <= end:
		mid = (start + end)/2
		if num == arr[mid]:
			return mid
		elif num > arr[mid]:
			start = mid + 1
		else:
			end = mid - 1
	return -1

print 'Enter element of sorted list'
arr = map(int, raw_input().split())

print 'Enter element to be search'
num = int(raw_input())

print binarysearch(arr, num)
