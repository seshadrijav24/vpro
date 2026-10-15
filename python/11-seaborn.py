"""
    seaborn
    *******
        develop rich/styled graphs
        built on top of "matplotlib"
        "less" coding able to develop "styled" graphs
        provides ready made "datasets"
"""
# lineplot
# import seaborn as sns
# import matplotlib.pyplot as plt
# tips = sns.load_dataset("tips")
# tips = tips.head()
# print(tips)
# sns.lineplot(data=tips, x="size", y="total_bill")
# plt.show()


# scatter plot
# import seaborn as sns
# import matplotlib.pyplot as plt
# tips = sns.load_dataset("tips")
# sns.scatterplot(data=tips, x="size", y="tip",hue="sex")
# plt.show()

# bar plot
# import seaborn as sns
# import matplotlib.pyplot as plt
# tips = sns.load_dataset("tips")
# sns.barplot(data=tips, x="day", y="total_bill")
# plt.show()


# histo
# import seaborn as sns
# import matplotlib.pyplot as plt
# tips = sns.load_dataset("tips")
# sns.histplot(tips["total_bill"],bins=20,kde=True)
# plt.show()



# heatmap
# import seaborn as sns
# import matplotlib.pyplot as plt
# flights = sns.load_dataset("flights")
# print(flights.head(10))
# pivot = flights.pivot(index="month",columns="year",values="passengers")
# sns.heatmap(pivot,annot=True,fmt="d",cmap="plasma")
# plt.show()

# import seaborn as sns
# print(sns.get_dataset_names())


