#All Assignment Operators & Bitwise Operators:-
x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))

print("\nInitial Values: x =", x, ", y =", y)

# 1. Assignment (=)
a = x
print("Assignment (=):", a)

# 2. Add and assign (+=)
x += y
print("After += :", x)

# 3. Subtract and assign (-=)
x -= y
print("After -= :", x)

# 4. Multiply and assign (*=)
x *= y
print("After *= :", x)

# 5. Divide and assign (/=)
x /= y
print("After /= :", x)

# 6. Floor divide and assign (//=)
x //= y
print("After //= :", x)

# 7. Modulus and assign (%=)
x %= y
print("After %= :", x)

# 8. Exponent and assign (**=)
x **= 2
print("After **= :", x)

# Bitwise operations (reset x for clarity)
x = int(input("\nEnter value of x for bitwise operations: "))

# 9. Bitwise AND (&=)
x &= y
print("After &= :", x)

# 10. Bitwise OR (|=)
x |= y
print("After |= :", x)

# 11. Bitwise XOR (^=)
x ^= y
print("After ^= :", x)

# 12. Right shift (>>=)
x >>= 1
print("After >>= :", x)

# 13. Left shift (<<=)
x <<= 2
print("After <<= :", x)


