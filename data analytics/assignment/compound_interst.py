
p = int(input("Enter the principal: "))
r = int(input("Enter the rate: "))
t = int(input("Enter the time: "))

A = p * (1 + r / 100) ** t
CI = A - p

print("Compound interest =", CI)
print("Total amount =", A)