"""
    pandas
    ******
        pandas is the python library
        pandas, used to deal tabular data
        excel sheet/csv sheets/json files
        pandas, able to "clean" the data
        pandas able to make data ready for visualization
"""

# Example-1
# import pandas as pd
# print(pd.__version__)


# Example-2
# import pandas as pd
# data = [10,20,30,40,50]
# res = pd.Series(data)
# res = pd.Series(data,index=["a","b","c","d","e"])
# res = pd.Series(data,index=["Std1","Std2","Std3","Std4","Std5"])

# res = pd.Series(data)
# res = res.to_string(index=False)
# print(res)

# Example-3
# import pandas as pd
# data = {
#     "rollno":[101,102,103,104,105],
#     "names":["Std1","Std2","Std3","Std4","Std5"],
#     "marks":[90,80,70,60,50]
# }
# res = pd.DataFrame(data)
# res = res.to_string(index=False)
# print(res)


# Example-4
import pandas as pd
data = pd.read_csv("students.csv")

# print(data)
# print(data.shape)
# print(data.columns)
# print(data.dtypes)


