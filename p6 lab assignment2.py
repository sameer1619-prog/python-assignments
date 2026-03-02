# Lab Assignment 2

def convert_to_upper(lines):
    for line in lines:
        print(line.upper())

# Taking input
lines = []
n = int(input("Enter number of lines: "))

for i in range(n):
    line = input()
    lines.append(line)

convert_to_upper(lines)