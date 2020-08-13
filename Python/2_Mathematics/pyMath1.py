# Python Example Appendix
# Optional extras:

# === Config Section [DO NOT CHANGE]===

# === End Config Section ===

# ///////////////////////////////////
# Example_1: ==Arithmetic==
# Description: Pretty straight forward.
# Division always results in a float
print("==Example_1==")
print("\n*(1a)*\n")
x = 1
y = 2
z = x + y #addition
print(z)

print("\n*(1b)*\n")
z = x - y #subtraction
print(z)

print("\n*(1c)*\n")
z = x * y #multiplication
print(z)

print("\n*(1d)*\n")
z = y / x #division
print(z)

print("\n*(1e)*\n")
#for rounding use //
x = 7.0
y = 5.0
z = x // y
print(z)

print("\n*(1f)*\n")
#modulo returns remainder
z = x % y
print(z)

# ///////////////////////////////////
# Example_2: ==Boolean Logic==
# Description: 1 == 0 = False.
print("==Example_2==")
print("\n*(1a)*\n")
x = True
y = False
z = x and y
print(z)
print("\n*(1b)*\n")
print(not x)
print("\n*(1c)*\n")
print(x or y)
print("\n*(1d)*\n")
print(x or not y)
