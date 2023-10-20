# Machine-level equation: (a & b) | (c ^ d)
a = 0b1010  # Binary representation of 10
b = 0b1100  # Binary representation of 12
c = 0b0110  # Binary representation of 6
d = 0b0011  # Binary representation of 3

result = (a & b) | (c ^ d)

# Print the result in binary and decimal format
print("Result in binary:", bin(result))
print("Result in decimal:", result)
