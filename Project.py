import random

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['!', '@', '#', '$', '%', '^', '&', '*', '>', '<']
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r','s','t','u','v','w','x','y','z']
letter1=['A','B','C', 'D', 'E', 'F', 'G' 'H', 'I', 'J', 'K',  'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
i = int(input("How many numbers do you want in your password? "))
j = int(input("How many special characters do you want in your password? "))
l = int(input("How many lower case letters do you want in your password? "))
u= int(input("How many upper case letters do you want in your password? "))
total_length = i + j + l+u

if total_length < 6:
    print("Password length must be at least 6 characters.")
elif total_length > 20:
    print("Password length must not exceed 20 characters.")
else:
    ourpass = []

for char in range(1, i+1):
    ourpass += random.choice(num)

for char in range(1, j+1):
    ourpass += random.choice(special)

for char in range(1, l+1):
    ourpass += random.choice(letter)
for char in range(1, u+1):
    ourpass += random.choice(letter1)
random.shuffle(ourpass)

password = "".join(ourpass)
#for char in ourpass:
    #password += char

print("Total Password length:",total_length)
print(f"Your generated password is: {password}")


