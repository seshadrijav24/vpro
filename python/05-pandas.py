"""
    pandas
    ******
        python module
        tabular data (rows & cols)
        excel sheets/csv files/json files
        able to "clean" the data
        make data ready for "visualization"
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

# res4 = pd.Series(data)
# res4 = res4.to_string(index=False)
# print(res4)

# Example-3
# import pandas as pd
# data = {
#     "roll_no":[101,102,103,104,104],
#     "name":["std1","std2","std3","std4","std5"],
#     "marks":[60,70,80,90,99]
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

# print(df.tail())
# print(df.tail(3))

# print(df["name"])
# print(df.name)

# print(df[["name","marks"]])

# print(df.loc[0])
# print(df.loc[0:2])  # 0,1,2

# print(df[df["marks"]<14])

# grades = ["A","B","C","D","E"]
# df["grades"] = grades
# df.to_csv("output.csv")

# print( df.drop("dept", axis=1) )

# ascending
# df = df.sort_values("marks")
# print(df)

# decending
# df = df.sort_values("marks",ascending=False)
# print(df)

# print(df["marks"].max())
# print(df["marks"].min())
# print(df["marks"].sum())
# print(df["marks"].mean())

# Example-5
# import pandas as pd
# students = pd.DataFrame({
#     "roll_no":[101,102,103,104],
#     "name":["std1","std2","std3","dtd4"]
# })
# marks = pd.DataFrame({
#     "roll_no":[101,102,103,105],
#     "marks":[60,70,80,90]
# })
# res1 = pd.merge(students,marks,on="roll_no",how="inner")
# print(res1)

# res2 = pd.merge(students,marks,on="roll_no",how="left")
# print(res2)

# res3 = pd.merge(students,marks,on="roll_no",how="right")
# print(res3)

# res4 = pd.merge(students,marks,on="roll_no",how="outer")
# print(res4)


# Example-6
# import pandas as pd
# df = pd.DataFrame({
#     "name":["std1","std2","std3","std4"],
#     "marks":[80,90,70,60],
#     "age":[20,21,22,23]
# })
# df["marks"] = 100
# print(df)

# df["marks"] = df["marks"] + 10
# print(df)

# df[["marks","age"]] = 0
# print(df)

# df.loc[0,"marks"] = 90
# print(df)

# Example-7
# import pandas as pd
# df = pd.DataFrame({
#     "Name" : ["Ram","Ram","Ravi","Ravi"],
#     "products":["Laptop","Mobile","Laptop","Mobile"],
#     "sales":[50000,20000,60000,30000]
# })
# print(df)
# print("---------------------------------------")
# res = df.pivot(index="Name",columns="products",values="sales")
# print(res)

# Example-8
import pandas as pd
df = pd.DataFrame({
    "Name":["Ram","Ravi","Anil","Kiran"],
    "marks":[80,None,90,None]
})
# print(df)

# df.drop(1,inplace=True)
# print(df)

# res1 = df.drop(1,inplace=False)
# print(res1)
# print(df)

# df.drop([0,2],inplace=True)
# print(df)

# df.fillna(100,inplace=True)
# print(df)

# df["marks"] = df["marks"].ffill()
# print(df)

# df["marks"] = df["marks"].bfill()
# print(df)

# df["marks"] = df["marks"].fillna(50)
# print(df)

# df["marks"] = df["marks"].fillna(df["marks"].mean())
# print(df)

# res = df.dropna()
# print(res)
# print(df)

# df.dropna(inplace=True)
# print(df)

# print(df.isnull())
# print(df.isna())

# print(df.isnull().sum())
