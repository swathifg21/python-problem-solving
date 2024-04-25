arr = [1, 2, 3, 4, 5]
print("Original list:", arr)

arr.append(6)
print("List after appending:", arr)

arr.insert(2, 10)
print("List after insertion:", arr)

arr.remove(3)
print("List after removal:", arr)

print("Element at index 3:", arr[2]) 

arr[2] = 8 
print("List after update:", arr)

print("List elements:")
for i in arr:
    print(i, end=' ')
