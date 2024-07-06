arr = []
num = int(input("enter no of elements in arr:"))

for i in range(num):
    numbers = int(input("enter numbers"))
    arr.append(numbers)

print("max nub in the given list is:" , max(arr))
print("min nub in the given list is:" , min(arr))