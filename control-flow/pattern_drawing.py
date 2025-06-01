
length = int(input("Enter the size of the pattern:"))

while length <= 0:
    length = int(input("Please enter a positive integer: "))
row = 0
while row < length:
    for col in range(length):
        print("*", end="")
    print()  
    row += 1
