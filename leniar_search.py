def linear_search(lst, target):

	store = len(lst)
	for i in range(store):
		if lst[i] == target:
			return i
	return None

def varify(index):
	if index is not None:
		print("target found at the list")
	else:
		print("target not found at the list")

lst = [2,34,4,56,7,8,9,67,56,4,4,6,8,5]

result = linear_search(lst, 7)

varify(result)

