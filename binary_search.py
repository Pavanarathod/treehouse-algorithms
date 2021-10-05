def binary_search(lst, target):
	first = 0
	last = len(lst) - 1
	print("first index", first)
	print("last index", last)

	while first <= last:
		midpoint = (first + last) // 2
		print("Current status of midpoint is ", midpoint)

		if lst[midpoint] == target:
			return midpoint

		elif lst[midpoint] < target:
			first = midpoint + 1
			print("first index", first)
		else:
			last = midpoint - 1
			print("last index", last)

	return None

def varify(index):
	if index is not None:
		print("target found at the list")
	else:
		print("target not found at the list")
lst = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(lst, 11)
varify(result)
