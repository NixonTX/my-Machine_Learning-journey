# # with open("ex.txt", "r") as file:
# #     content = file.read()
# #     print(content)

# # # with open("ex.txt", "w") as file:
# # #     file.write("Hello, How are You?")
# # #     file.write("\nnext line")

# # # with open("ex.txt", "a") as file:
# # #     file.write("\nMore..")

# # with open("ex.txt", "r") as file:
# #     for line in file:
# #         print(line.strip())

# # with open("ex.txt", "r") as file:
# #     lines = file.readlines()
# #     print(lines)

# with open("example.bin", "wb") as file:
#     file.write(b"Binary data")

# with open("example.bin", "rb") as file:
#     binary_content = file.read()
#     print(binary_content)

# import os

# if os.path.exists("ex.txt"):
#     print("File exists")
# else:
#     print("file not found!")


from my_package import module1, module2

print(module1.wish("Armin"))
print(module2.motivate("Berlordt"))