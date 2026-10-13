"""
    matplotlib
    **********
        matplotlib used to display graphs / plots
        Ex.
                Line Plot
                Bar Chart
                Pie Plot
                Scatter Plot
                HeatMap
                Subplots
                ---
                ---
                ---
"""
# # Line Plot
# import matplotlib.pyplot as plt

# # x-axis
# months = ["Jan","Feb","Mar","Apr","May","June"]

# # y-axis
# emp1 = [55,60,65,62,72,80]
# emp2 = [60,65,62,72,80,85]

# # reserve space
# plt.figure(figsize=(10,5))


# # line plot
# plt.plot(months,emp1,marker='o',linestyle="-",linewidth=2,label="emp1")
# plt.plot(months,emp2,marker='x',linestyle="--",linewidth=3,label="emp2",color="red")

# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.title("Line Plot Demo")

# plt.xticks(rotation=45)
# plt.ylim(0,100)
# plt.grid()
# plt.legend()


# plt.annotate("emp1 highest sales",
#              xy=("June",80),
#              xytext=("May",90),
#              arrowprops=dict(arrowstyle="->"))

# plt.savefig("lineplot.png")

# # show the graph
# plt.show()



# # Bar Chart
# import matplotlib.pyplot as plt

# # x-axis
# months = ["Jan","Feb","Mar","Apr","May","June"]

# # y-axis
# sales = [120,150,180,140,200,230]
# profits = [30,40,55,35,65,80]

# plt.figure(figsize=(10,5))

# bars = plt.bar(months,sales,color="black")
# bars1 = plt.bar(months,profits,color="red")

# plt.xlabel("Months")
# plt.ylabel("Sales & Profits")
# plt.title("Months - Sales Analysis")
# plt.ylim(0,300)

# plt.grid(axis="y",linestyle="--",alpha=0.5)

# for bar in bars:
#     value = bar.get_height() + 4
#     plt.text(bar.get_x() + (bar.get_width()/2) , value, str(value), ha="center",va="center")


# for bar in bars1:
#     value = bar.get_height() + 4
#     plt.text(bar.get_x() + (bar.get_width()/2) , value, str(value), ha="center",va="center")


# plt.savefig("bar.png")

# plt.show()


# Scatter Plot (Graph Sheets)
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("scatter_ex.csv")

# hours = df["hours"]
# marks = df["marks"]

# plt.scatter(hours,marks,marker="^",c="red",s=30)
# plt.xlabel("Hours")
# plt.ylabel("Marks")
# plt.title("Hours - Marks")
# plt.grid()
# plt.savefig("scatter.png")
# plt.show()


# Histogram
# import matplotlib.pyplot as plt
# marks = [45,50,52,55,58,
#          60,62,65,67,68,
#          70,72,75,78,80,
#          82,85,88,90,92]
# # bins - 5
# # 92 - 45 = 47 / 5 = 9
# # bin1 - 45 - 54
# # bin2 - 54 - 63
# # bin3 - 63 - 72
# # bin4 - 72 - 81
# # bin5 - 81 - last
# plt.hist(marks,bins=5)
# plt.title("Students Marks Distribution")
# plt.xlabel("Marks")
# plt.ylabel("Students")
# plt.savefig("histo.png")
# plt.show()

# Subplots
# import matplotlib.pyplot as plt

# plt.subplot(2,2,1)
# plt.plot([1,2,3],[10,20,30])
# plt.xlabel("Hours")
# plt.ylabel("Marks")
# plt.title("Line Plot")

# plt.subplot(2,2,2)
# plt.bar(["Jan","Feb"],[100,200])
# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.title("Bar Chart")

# plt.tight_layout()
# plt.savefig("sub.png")

# plt.show()


# pie chart
# import matplotlib.pyplot as plt
# expenses = [30,40,15,10,5]
# categories = ["Rent","Salaries","Marketing","Food","Other"]
# colors = ["red","blue","green","orange","purple"]
# explode = [0,0.1,0,0,0]
# plt.pie(expenses,labels=categories,colors=colors,explode=explode,startangle=90,autopct='%1.2f%%')
# plt.title("Demo Pie Chart")
# plt.legend()
# plt.savefig("pie.png")
# plt.show()


#box-plot (analysis 1st quarter, half year, 3rd querter,.....)
# import matplotlib.pyplot as plt

# python_marks = [45,50,52,55,58,60,65,68,70,72]
# java_marks = [40,48,50,55,60,62,65,70,75,90]
# sql_marks = [50,55,58,60,62,65,68,70,72,95]

# plt.boxplot([python_marks,java_marks,sql_marks])
# plt.xticks([1,2,3],["Python","Java","SQL"])
# plt.title("Subject wise marks distribution")
# plt.ylabel("Marks")
# plt.grid(axis='y',linestyle="--",alpha=0.5)
# plt.savefig("box.png")
# plt.show()


# heatmap
# python std1 - 90(dark green). std2 - 60(green). std3 - 40(light green)
# import matplotlib.pyplot as plt
# students = ["Std1","Std2","Std3","Std4"]
# subjects = ["Python","Java","SQL","React"]
# marks = [[80,70,85,75],
#          [90,85,88,92],
#          [60,65,70,68],
#          [85,90,92,88]]
# plt.imshow(marks,cmap="viridis")        # viridis, plasma,magma, cividis,coolwarm,
# plt.xticks(range(len(subjects)),subjects)
# plt.yticks(range(len(students)),students)
# plt.colorbar(label="marks")
# plt.title("Marks Distribution")
# plt.savefig("heat.png")
# plt.show()

