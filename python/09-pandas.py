"""
    pandas
    ******
        deals the tablular data (rows & cols)
        deals the excel/csv/json files
        cleans the data before visulization
        pip install pandas
        import pandas as pd
"""

# Example-1
# import pandas as pd
# print(pd.__version__)

# Example-2
# import pandas as pd
# data = [10,20,30,40,50]
# res = pd.Series(data)
# print(res)

# res1 = pd.Series(data,index=["a","b","c","d","e"])
# print(res1)

# res2 = pd.Series(data,index=["std1","std2","std3","std4","std5"])
# print(res2)

# res3 = pd.Series(data)
# res3 = res3.to_string(index=False)
# print(res3)



# Example-3
# import pandas as pd
# data = {
#     "rollno":[101,102,103,104,105],
#     "names":["std1","std2","std3","std4","std5"],
#     "marks":[40,50,60,70,80]
# }
# df = pd.DataFrame(data)
# print(df)


# Example-4
# import pandas as pd
# df = pd.read_csv("students.csv")
# print(df)
# print(df.shape)
# print(df.columns)
# print(df.dtypes)

# print(df.head())
# print(df.head(2))
# print(df.head(1))

# print(df.tail())
# print(df.tail(2))
# print(df.tail(4))

# print(df["name"])
# print(df.marks)

# print(df[["name","marks"]])

# print(df.loc[0])
# print(df.loc[1])
# print(df.loc[0:3])      # 0,1,2,3 included

# grade = ["A","B","C","D","E"]
# df["grade"] = grade
# print(df)

# print( df.drop("dept",axis=1) )

# print( df[df["marks"]<14] )

# Adcending Order
# df = df.sort_values("marks")
# print(df)

# Decending Order
# df = df.sort_values("marks",ascending=False)
# print(df)

# print(df["marks"].max())
# print(df["marks"].min())
# print(df["marks"].sum())
# print(df["marks"].mean())

# attandance = [95,90,85,80,75]
# df["attandance"] = attandance
# df.loc[0,"marks"] = 90
# df.to_csv("output.csv")



# Example-5
# import pandas as pd
# df = pd.read_csv("emps.csv")
# print(df)
# print(df.groupby("dept")["salary"].sum())
# print(df.groupby("dept")["salary"].max())
# print(df.groupby("dept")["salary"].min())
# print(df.groupby("dept")["salary"].mean())

# Example-6
# import pandas as pd
# students = pd.DataFrame({
#     "student_id":[101,102,103,104],
#     "name":["std1","std2","std3","std3"]
# })
# marks = pd.DataFrame({
#     "student_id":[101,102,103,105],
#     "marks":[80,90,75,88]
# })
# res = pd.merge(students,marks,on="student_id",how="inner")
# print(res)

# res1 = pd.merge(students,marks,on="student_id",how="left")
# print(res1)

# res2 = pd.merge(students,marks,on="student_id",how="right")
# print(res2)


# res3 = pd.merge(students,marks,on="student_id",how="outer")
# print(res3)

