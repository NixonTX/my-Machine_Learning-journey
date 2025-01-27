for i in range(1, 5):
    print(f"count: {i}")

print("=============")

count = 0
while count < 5:
    print(f"count: {count}")
    count += 1

print("=============")

for n in range(1, 6):
    if n == 3:
        continue
    print(n)
else:
    print("done")

print("=============")

def add(a, b= 2):
    return a+b

print(add(3, 2))
print(add(4))

print("=============")

# args for multiple positional args
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 3, 4))
print(multiply(1, 5, 5))

print("=============")

def greet(*names):
    for name in names:
        print(f"Hello, {name}!")

greet("Ark", "Bin", "Con")

print("=============")

def greet(greeting, *names):
    print(greeting)
    for n in names:
        print(f"- {n}")

greet("Hi pals:", "Ali", "Ber", "Can")

print("=============")

sqr = lambda x: x ** 2
print(sqr(4))

qube = lambda x: x**3
print(qube(3))

nums = [1, 2, 3, 4, 5, 6, 7, 8]
Tube = filter(lambda T: T % 2 == 0, nums)
print(list(Tube))

print("=============")

# try:
#     num = int(input("Enter a num: "))
#     print(10/num)
# except ZeroDivisionError:
#     print("Division by zero not invented")
# finally:
#     print("Good luck, keep going.")

# print("=============")

# try:
#     result = 10/0
# except Exception as e:
#     print(f"An error occurred: {e}")

# print("=============")

def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18")
    return "Access granted"

try:
    print(check_age(17))
except ValueError as e:
    print(e)