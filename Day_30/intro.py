# try:
#     file = open("Day_30/test.txt")
#     a_dict = {"key":"value"}
#     print(a_dict["key"])

# except FileNotFoundError:
#     idk = open("Day_30/test.txt", mode="a") 
#     idk.write("test")

#     print("File error")
# except KeyError as error_msg:
#     print(f"key error is: {error_msg}")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file was closed")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3m!")
bmi = weight / height ** 2