# Example-1
# age = 20
# if age >= 18:
#     print("Major !!!")


# Example-2
# age = 16
# if age >= 18:
#     print("Major !!!")
# else:
#     print("Minor !!!")

# Example-3
# marks = 75
# if marks >= 90:
#     print("A")
# elif marks >= 75:
#     print("B")
# elif marks >= 60:
#     print("C")
# else:
#     print("D")


# # Example-4
# x = 10
# if x > 5:
#     print("A")

# if x > 8:
#     print("B")

# if x > 15:
#     print("C")


# AND
# True AND True -- True
# True AND False -- False
# False AND True -- False
# False AND False -- False

# OR
# True OR True -- True
# True OR False -- True
# False OR True -- True
# False AND False -- False

# Example-5
# age = 25
# salary = 50000
# if age >= 18 and salary >= 30000:
#     print("Eligible for Loan")
# else:
#     print("Not Eligible for Loan")

# Example - 6
# logged_in = False
# if not logged_in:
#     print("Please Login")
# else:
#     print("Logout")

# Example-7
# age = 25
# has_id = True
# if age >= 18:
#     if has_id:
#         print("Entry Granted !!!")
#     else:
#         print("id not matched")
# else:
#     print("age restriction")

# Example-8
# age = 20
# if age >= 18:
#     if age >= 21:
#         print("Enter !!!")
#     else:
#         print("Restricted !!!")

# Example-9
# "", False, None, 0, 0.0, [], (), {}, set() - Falsy
# username=""
# if username:
#     print("Login Success")
# else:
#     print("Please Login")


# # Example-10
# res = None
# if res is None:
#     print("Empty !!!")

# Example-11
# list1 = [10,20,30]
# list2 = [10,20,30]
# print(list1 == list2)
# print(list1 is list2)


# Example-12
# lang = ["Java","ML","DL"]
# if "ML" in lang:
#     print("Found !!!")
# else:
#     print("Not Found !!!")

# Example-13
# str = "Machine Learning"
# if "Machine" in str:
#     print("Found !!!")

# Example-14
# age = 25
# if 18 <= age <= 60:                 # age >= 18 and age <=60
#     print("Allowed to work !!!")
# else:
#     print("Not Allowed")


# # Example-15
# x = 10
# 5 < x < 20      # x > 5 and x < 20
#                 # 5 < x and x < 20


# Example - 16
# age = 20
# res = "Major" if age>18 else "Minor"
# print(res)

# Example - 17
# num1 = 100
# num2 = 200
# num3 = 300
# res = (num1) if (num1>num2 and num1>num3) else (num2) if (num2>num3) else (num3)
# print(res)

# Example - 18
x = 10
if x / 0 or x > 5:
    print("Hello")
else:
    print("Welcome")