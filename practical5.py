# Take input from user
numbers = tuple(map(int, input("Enter integers separated by space: ").split()))

# a) Print total number of items
print("Total number of items:", len(numbers))

# b) Print last item
print("Last item in tuple:", numbers[-1])

# c) Print tuple in reverse order
print("Tuple in reverse order:", numbers[::-1])

# d) Check if 5 exists
if 5 in numbers:
    print("Yes, 5 exists in the tuple.")
else:
    print("No, 5 does not exist in the tuple.")

# e) Remove first and last items, sort remaining
if len(numbers) > 2:
    new_tuple = numbers[1:-1]
    sorted_tuple = tuple(sorted(new_tuple))
    print("After removing first and last, sorted tuple:", sorted_tuple)
else:
    print("Not enough elements to remove first and last.")