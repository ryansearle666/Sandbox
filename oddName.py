"""Ryan Searle"""

user_name = str(input("Insert name: "))
while len(user_name) <= 0:
    print("Insert Valid Name")
    user_name = str(input("Insert name: "))
print(user_name[1: :2])
