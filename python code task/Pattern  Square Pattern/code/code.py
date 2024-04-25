def calculate_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total
num = int(input("Enter a number: "))
result = calculate_sum(num)
print(f"The sum of numbers from 0 to {num} is {result}.")

