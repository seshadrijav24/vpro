# Example-1
# for i in range(10):     # 0 included and 10 excluded
#     if i == 5:
#         # break         # 0 1 2 3 4
#         continue        # 0 1 2 3 4 6 7 8 9
#     print(i)            

# Example-2
# for i in range(5):          # pass - nothing 
#     pass


# Example-3
# for i in range(5):
#     print(i)
# else:
#     print("for loop completed")     # 0 1 2 3 4 for loop completed

# Example-4
# for i in range(5):
#     if i == 3:
#         break
#     print(i)                # 0 1 2
# else:
#     print("Completed !!!")


# Example-5
# for i in range(5):            # 0 - 4
#     pass

# print(i)      # 4

# Example-6    
# i = 1
# while i<=5:
#     print(i)
#     i += 1


# Example-7
# list1 = [10,20,30,40,50]
# list2 = [100,200,300,400,500]

# for element in list1:
#     print(element,end=" | ")

# for index,element in enumerate(list2):
#     print(index,element,sep="---->")


# for element1,element2 in zip(list1,list2):
#     print(element1,element2)

# Example-8
# for i in range(3):
#     for j in range(2):      # i=0  j=0,1
#         print(i,j)          # i=1. j=0,1
#                             # i=2  j=0,1


# Example-9
# for i in range(10,1,-2):        # 10 8 6 4 2
#      print(i)

# for i in range(0,10,2):
#      print(i)                   # 0 2 4 6 8


# Example-10
# match (pattren matching)
# day = 10
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case _:
#         print("No Match")

# Example-11
# for _ in range(10):
#     print(_)


# _ = 100
# print(_)