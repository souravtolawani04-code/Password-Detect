print("Hello welcome to password checker")
print("_________________________________")

print("")

number = input("Enter the password : ")

num_len = len(number)

isNumber = False

for char in number:
    if char.isdigit():
        isNumber = True

if (num_len >=8 and isNumber == True):
    print("Strong Password")
else:
    print("Weak Password")

print("Thank you for comming here❤️")

