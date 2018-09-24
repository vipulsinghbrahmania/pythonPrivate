def leftRotate(arr, d): # call rotate func d times
	for i in range(d):
		rotate(arr)

def rotate(arr): # move one digit to the left at a time
	temp = arr[0]
	for i in range(len(arr)-1):
		arr[i] = arr[i+1]
	arr[len(arr)-1] = temp

# Driver test code
arr = [1, 2, 3, 4, 5, 6, 7]

print("Orig Array  --> ", arr)
leftRotate(arr, 3)
print("Left Rotate --> ", arr)
