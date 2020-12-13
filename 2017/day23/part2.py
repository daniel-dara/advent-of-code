import sympy

# After studying the problem input, the original code is counting the number of composite numbers in the range
# [106,700, 123,700].
print(sum(not sympy.isprime(i) for i in range(106700, 123700 + 1, 17)))
