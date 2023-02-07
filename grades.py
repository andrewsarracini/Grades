from matplotlib import axes, colors
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib import colors


from pyparsing import col, line

my_dict = {'First Year': [8, 3, 6, 0, 8, 6, 5, 4, 3, 6],
           'Second Year': [9, 10, 11, 11, 8, 9, 8, 8, 9, 3],
           'Third Year': [4, 8, 7, 8, 11, 7, 9, 11, 11],
           'Fourth Year': [6, 11, 10, 12, 12, 11, 11, 12],
           'Fifth Year': [12, 10, 11, 11],
           'Postbac': [12]}

grades_df = pd.DataFrame({key: pd.Series(value)
                         for key, value in my_dict.items()})

all_avg = grades_df.mean()

fir_avg = grades_df['First Year'].mean()
sec_avg = grades_df['Second Year'].mean()
thir_avg = grades_df['Third Year'].mean()
four_avg = grades_df['Fourth Year'].mean()
fif_avg = grades_df['Fifth Year'].mean()

total_avg = (grades_df['First Year'].sum() + grades_df['Second Year'].sum() + grades_df['Third Year'].sum() +
             grades_df['Fourth Year'].sum() + grades_df['Fifth Year'].sum() + grades_df['Postbac'].sum()) / 42

''' Separating the data by semester, 2D array '''
sem_grades = [[8, 3, 6, 0, 8],
              [6, 5, 4, 3, 6],
              [9, 10, 11, 11, 8],
              [9, 8, 8, 9, 3],
              [4, 8, 7, 8, 11],
              [7, 9, 11, 11],
              [6, 11, 10, 12],
              [12, 11, 11, 12],
              [12, 10, 11, 11, 12]]

sem_avgs = [np.average(sem) for sem in sem_grades]
sem_sum = [sum(grade) for grade in sem_grades]


''' Separating the data by academic year '''
fig, ax = plt.subplots(
    5, 1, sharex=True, sharey=True)

Y1 = sem_grades[0] + sem_grades[1]
Y2 = sem_grades[2] + sem_grades[3]
Y3 = sem_grades[4] + sem_grades[5]
Y4 = sem_grades[6] + sem_grades[7]
Y5 = sem_grades[8]

''' Histograms good for visualizing, but my gradient won't work '''
''' Seaborn 'Count Plot' might be a much simpler way of doing this! '''

ax[0].hist(
    Y1, width=0.4, bins=np.arange(14), edgecolor='k')
ax[0].set_title('Year 1')
ax[1].hist(
    Y2, width=0.4, bins=np.arange(14), edgecolor='k')
ax[1].set_title('Year 2')
ax[2].hist(
    Y3, width=0.4, bins=np.arange(14), edgecolor='k')
ax[2].set_title('Year 3')
ax[3].hist(
    Y4, width=0.4, bins=np.arange(14), edgecolor='k')
ax[3].set_title('Year 4')
ax[4].hist(
    Y5, width=0.4, bins=np.arange(14), edgecolor='k')
ax[4].set_title('Year 5')
ax[4].set_xlabel('Grades')

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
labels = ['F', 'D-', 'D', 'D+', 'C-', 'C',
          'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+']

ax[4].set_xticks(x, labels)

plt.show()

# ''' Bar Graphs might allow me to add a gradient'''
# ax[0].bar(Y1, [1, 0, 0, 2, 1, 1, 3, 0, 2, 0, 0, 0, 0],
#           width=0.4, align='center')
# ax[0].set_title('Year 1')

# plt.show()

''' New scatter plot showing the progression of semester averages '''

time_series = ['Year 1, Sem 1',
               'Year 1, Sem 2',
               'Year 2, Sem 1',
               'Year 2, Sem 2',
               'Year 3, Sem 1',
               'Year 3, Sem 2',
               'Year 4, Sem 1',
               'Year 4, Sem 2',
               'Year 5, Sem 1 + Postbac']


df = pd.DataFrame(dict(time_series=time_series, sem_avgs=sem_avgs))
print(df)

fig, ax = plt.subplots()

''' This is a way to map each point to certain colours, but the line connecting the points won't show up '''

# colours = {'Year 1, Sem 1': 'red', 'Year 1, Sem 2': 'red', 'Year 2, Sem 1': 'orange', 'Year 2, Sem 2': 'orange', 'Year 3, Sem 1': 'gold', 'Year 3, Sem 2': 'gold',
#            'Year 4, Sem 1': 'cornflowerblue', 'Year 4, Sem 2': 'cornflowerblue', 'Year 5, Sem 1 + Postbac': 'green'}

# grouped = df.groupby('time_series')
# for key, group in grouped:
#     group.plot(ax=ax, kind='scatter', x='time_series',
#                y='sem_avgs', label=key, color=colours[key])


''' This method is more simple, but it connects the points '''
''' Still working on colour-coding with plt.plot though '''

plt.plot(time_series, sem_avgs, marker='.', markersize=10)


plt.xticks(rotation=90)
plt.yticks(np.arange(4, 13, step=1))
plt.xlabel('Academic Semester')
plt.ylabel('Grade point Average')
plt.title('Post Secondary GPA')

plt.show()
