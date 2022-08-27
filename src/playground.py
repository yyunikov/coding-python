print("==========================")
# power of 2
print("Outputting the power of 2:")
x = 0b00000000000000000000000000000010
largest_power_of_2 = pow(2, 31)
current = x
while current < largest_power_of_2:
    current = current << 1
    print(current)

print("==========================")
# power of 4
print("Outputting the power of 4:")
x = 0b00000000000000000000000000000100
current = x
while current < largest_power_of_2:
    current = current << 2
    print(current)

print("==========================")