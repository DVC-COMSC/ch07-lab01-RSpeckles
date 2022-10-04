
# ******************************
# Make your Code
# ******************************
numbers = []
while len(numbers) < 5:
    try:
        numbers.append(int(input("Enter a number: ")))
    except ValueError:
        print("Input must be a numeric value")

shortest = numbers[0]
longest = numbers[0]

for i in range(5):
    if numbers[i] < shortest:
        shortest = numbers[i]
    elif numbers[i] > longest:
        longest = numbers[i]

sum = 0

for i in range(5):
    sum += numbers[i]

sum = sum - shortest - longest
print(sum)
