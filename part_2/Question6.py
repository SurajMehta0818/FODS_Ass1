# Find numbers between 1500 and 2000 divisible by 7 and multiple of 5
result = []
for num in range(1500, 2001):
    if num % 7 == 0 and num % 5 == 0:
        result.append(num)

# Display the results
print("Numbers between 1500 and 2000 divisible by 7 and multiples of 5:")
print(result)