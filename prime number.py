# Take valid input using while loop
while True:
    try:
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))
        
        if start < 0 or end < 0:
            print("Please enter positive numbers only.")
        elif start > end:
            print("Starting number must be less than or equal to ending number.")
        else:
            break
    except ValueError:
        print("Invalid input! Please enter integers only.")

print(f"\nPrime numbers between {start} and {end} are:")

# Check for prime numbers using for loop
for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            print(num)