# Hard-coded basic calculator without functions
# Example calculations with two sets of numbers

# First set of calculations
x = 10
y = 3

print("=== Basic Calculator Demo ===")
print(f"Numbers: x = {x}, y = {y}")
print(f"Addition: {x} + {y} = {x + y}")
print(f"Subtraction: {x} - {y} = {x - y}")
print(f"Multiplication: {x} * {y} = {x * y}")
print(f"Division: {x} / {y} = {x / y}")

# Second set of calculations with division by zero handling
x2 = 10
y2 = 0

print("\n=== Division by Zero Demo ===")
print(f"Numbers: x = {x2}, y = {y2}")
print(f"Addition: {x2} + {y2} = {x2 + y2}")
print(f"Subtraction: {x2} - {y2} = {x2 - y2}")
print(f"Multiplication: {x2} * {y2} = {x2 * y2}")

# Handle division by zero
if y2 == 0:
    print("Division: Cannot divide by zero")
else:
    print(f"Division: {x2} / {y2} = {x2 / y2}")

# Additional examples with different numbers
x3 = 15
y3 = 4

print("\n=== Additional Examples ===")
print(f"Numbers: x = {x3}, y = {y3}")
print(f"Addition: {x3} + {y3} = {x3 + y3}")
print(f"Subtraction: {x3} - {y3} = {x3 - y3}")
print(f"Multiplication: {x3} * {y3} = {x3 * y3}")
print(f"Division: {x3} / {y3} = {x3 / y3}")

# Decimal examples
x4 = 7.5
y4 = 2.5

print("\n=== Decimal Examples ===")
print(f"Numbers: x = {x4}, y = {y4}")
print(f"Addition: {x4} + {y4} = {x4 + y4}")
print(f"Subtraction: {x4} - {y4} = {x4 - y4}")
print(f"Multiplication: {x4} * {y4} = {x4 * y4}")
print(f"Division: {x4} / {y4} = {x4 / y4}")
