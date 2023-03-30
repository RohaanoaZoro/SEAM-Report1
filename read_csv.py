# importing csv module
import pandas as pd
import numpy as np


import matplotlib.pyplot as plt

# csv file name
filename = "E1_train_knowledge.csv"

df = pd.read_csv(filename)
df = df[1:]


df = df.astype({'Duration (in seconds)':'int','T1_First Click':'float', 'T1_Last Click': 'float'})

df["TimeTaken"] = df['T1_First Click'] - df['T1_Last Click']
df = df.drop(columns=['T1_First Click', 'T1_Last Click', 'Q36'])
# print(df)


q3_1 = {}
for temp in df['Q3_1']:
    if temp in q3_1:
        q3_1[temp]+=1
    else:
        q3_1[temp]=1

print(q3_1)


q3_2 = {}
for temp in df['Q3_2']:
    if temp in q3_2:
        q3_2[temp]+=1
    else:
        q3_2[temp]=1

print(q3_2)

q3_3 = {}
for temp in df['Q3_3']:
    if temp in q3_3:
        q3_3[temp]+=1
    else:
        q3_3[temp]=1

print(q3_3)

q3_4 = {}
i=0
for temp in df['Q3_4']:
    if temp == 'Adequate':
        i+=1

    if temp in q3_4:
        q3_4[temp]+=1
    else:
        q3_4[temp]=1

print(q3_4)
github = {}
for temp in df['Github']:
    if temp in github:
        github[temp]+=1
    else:
        github[temp]=1
print(github)


stride = {}
for temp in df['STRIDE']:
    if temp in stride:
        stride[temp]+=1
    else:
        stride[temp]=1
print(stride)

github_good = {}
j=0
k=0
l=0
arr = df['Q3_4'].values
for temp in df['STRIDE']:
    if arr[j] == 'Limited' or arr[j] == 'Very Limited':
        k+=1
        if temp in github_good:
            github_good[temp]+=1
        else:
            l+=1
            github_good[temp]=1

    j+=1

github_good['x']=0
github_good['y']=0
github_good['z']=0

print(k, l)


def plotBarGraph(tick_label, height, xlabel, ylabel, title, colors):
    # # x-coordinates of left sides of bars 
    left = [1, 2, 3, 4, 5]
    
    # plotting a bar chart
    plt.bar(left, height, tick_label = tick_label, width = 0.8, color = colors)
    
    # naming the x-axis
    plt.xlabel(xlabel)
    plt.xticks(rotation=90)

    # naming the y-axis
    plt.ylabel(ylabel)
    # plot title
    plt.title(title)
    
    # function to show the plot
    plt.show()

def StackedBar(x, y, xtitle):
    width = 0.6  # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()
    bottom = np.zeros(5)

    for diagramType, diagramValue in y.items():
        p = ax.bar(x, diagramValue, width, label=diagramType, bottom=bottom)
        bottom += diagramValue

        ax.bar_label(p, label_type='center')

    ax.set_title(xtitle)
    ax.legend()

    plt.show()

def SimplePlot(x, y):
    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.set(xlabel='Users', ylabel='time (s)',
        title='Time Taken')
    ax.grid()

    fig.savefig("test.png")
    plt.show()



# github_labels = ["Internships", "professional experiences", "Some Course", "Devops engineer", "Full Course"]
# colors = ['cornflowerblue', 'royalblue']
# plotBarGraph(list(github.keys()), list(github.values()), "GitHub Experince", "Count", "GitHub Knowledge", colors)


stride_labels = ["Novice", "Tried Tools", "some lectures or course", "professional", "Full Knowledge of tools"]
colors = ['firebrick', 'lightcoral']
plotBarGraph(stride_labels, list(stride.values()), "STRIDE Experince", "Count", "STRIDE Knowledge", colors)

# github_labels = ["Novice", "Tried Tools", "some lectures or course", "professional", "Full Knowledge of tools"]
# colors = ['violet', 'purple']
# plotBarGraph(github_labels, list(github_good.values()), "STRIDE Experince", "Count", "STRIDE Knowledge", colors)


# y = {
#     "Sequence Diagram":np.array([17, 17, 32, 25, 2]),
#     "Component Diagram":np.array([17, 22, 38, 13, 3]),
#     "Deployment Diagrams":np.array([20, 37, 25, 10, 1]),
#     "Data Flow Diagrams":np.array([15, 22, 26, 24, 6]),
# }
# x = ['Very Limited','Limited', 'Adequate', 'Good', 'Very Good']
# StackedBar(x, y, "Diagram Knowledge")


# SimplePlot(np.arange(0, len(df['Duration (in seconds)']), 1, dtype=int), df['Duration (in seconds)'] )

