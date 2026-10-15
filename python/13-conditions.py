# Example-1 (if condition)
# age = 20
# if age >= 18:
#     print("Eligible !!!")


# Example-2 (if-else)
# age = 16
# if age >= 18:
#     print("Major !!!")
# else:
#     print("Minor !!!")

# if - elif - else
# Example-3
# marks = 75
# if marks >= 90:
#     print("A")
# elif marks >=75:
#     print("B")
# elif marks >= 60:
#     print("C")
# else:
#     print("D")

# Example-4
# Output (AB)
# x = 10
# if x > 5:
#     print("A")
# if x > 8:
#     print("B")
# if x > 15:
#     print("C")

# Example-5
# Output : A
# x = 10
# if x > 5:
#     print("A")
# elif x > 8:
#     print("B")
# elif x > 15:
#     print("C")

# Example-6
# age = 25
# salary = 50000
# if age>=18 and salary>=30000:
#     print("Eligible for Loan")
# else:
#     print("Not Eligible")

# Example-7
# age = 25
# is_citizen = True
# if age >=18 and is_citizen:
#     print("Eligible for Vote !!!")
# else:
#     print("Not Eliglible")

# Example-8
# age = 17
# has_permission = True
# if age>=18 or has_permission:
#     print("Allowed !!!")


# Example-9
# age = 25
# salary = 20000
# exp = 5
# if age >= 18 and (salary >=30000 or exp>=3):
#     print("Eligible for Loan")
# else:
#     print("No Eligible for Loan")

# Example-10
# logged_in = False
# if not logged_in:
#     print("Please Login")
# else:
#     print("Logout")

# Example-11
# age = 25
# has_id = True
# if age >= 18:
#     if has_id:
#         print("Entry Allowed")


# Example-12
# age = 20
# has_id = False
# if age >= 18:
#     if has_id:
#         print("Entry Allowed")
#     else:
#         print("Restricted !!!")
# else:
#     print("Not Eligible")

# Example-13
# age = 20
# if age >= 18:
#     if age >= 21:
#         print("Enter !!!")
#     else:
#         print("Restricted !!!")

# Example-14
# username = "admin"
# if username == "admin":
#     print("Admin Login !!!")
# else:
#     print("User Login !!!")

# Example-15
# "" , None , 0, 0.0, [], (), {}, set() - Falsy
# username = ""           # Falsy Value
# if username == "admin":
#     print("Admin Login !!!")
# else:
#     print("User Login !!!")


# Example-16
# items = []
# if items:
#     print("Availble !!!")
# else:
#     print("Empty !!!")

# Example-17
# x = 0
# if x:
#     print("Hello")
# else:
#     print("Welcome")

# Example-18
# x = "0"
# if x:
#     print("Hello")
# else:
#     print("Welcome")

# Example-19
# result = None
# if result:
#     print("Empty")
# else:
#     print("Hello")

# Example-20
# result = None
# if result is None:
#     print("Empty !!!")        # insted of == we can use is

# Example-21
# list1 = [10,20,30]
# list2 = [10,20,30]
# print(list1 == list2)
# print(list1 is list2)

# Example-22
# lang = ["Java","ML","Python"]
# if "Python" in lang:
#     print("Found !!!")
# else:
#     print("Not Found !!!")


# Example-23
# str = "MachineLearning"
# if "Machine" in str:
#     print("Found !!!")

# Example-24
# age = 25
# if 18 <= age <= 60:                 # age >= 18 and age <=60
#     print("Work !!!")
# else:
#     print("Not Eligible !!!")


# Example-25
# age = 20
# res = "Major" if age>=18 else "Minor"
# print(res)


# Example-26
# num1 = 100
# num2 = 200
# num3 = 300
# res = num1 if (num1>num2 and num1>num3) else num2 if (num2>num3) else num3
# print(res)


# Example-27
# x = 10
# try:
#     if x / 0 or x > 5:
#         print("Hello")
#     else:
#         print("Welcome")
# except:
#     print("Exception")