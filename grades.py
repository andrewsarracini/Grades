from re import S
from turtle import width
from matplotlib import axes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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


''' Separating the data by semester, 2D array'''
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
print(sem_avgs)

''' Separating the data by academic year'''
fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(
    6, 1, sharex=True, sharey=True)

Y1 = sem_grades[0] + sem_grades[1]
Y2 = sem_grades[2] + sem_grades[3]
Y3 = sem_grades[4] + sem_grades[5]
Y4 = sem_grades[6] + sem_grades[7]
Y5 = sem_grades[8]

'''Making a *better* histogram'''

ax1.hist(Y1, width=0.4, bins=np.arange(14), edgecolor='k')
ax1.set_title('Year 1')
ax2.hist(Y2, width=0.4, bins=np.arange(14), edgecolor='k')
ax2.set_title('Year 2')
ax3.hist(Y3, width=0.4, bins=np.arange(14), edgecolor='k')
ax3.set_title('Year 3')
ax4.hist(Y4, width=0.4, bins=np.arange(14), edgecolor='k')
ax4.set_title('Year 4')
ax5.hist(Y5, width=0.4, bins=np.arange(14), edgecolor='k')
ax5.set_title('Year 5')
ax5.set_xlabel('Grades')

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
labels = ['F', 'D-', 'D', 'D+', 'C-', 'C',
          'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+']

ax5.set_xticks(x, labels)

time_series = ['Year 1, Sem 1',
               'Year 1, Sem 2',
               'Year 2, Sem 1',
               'Year 2, Sem 2',
               'Year 3, Sem 1',
               'Year 3, Sem 2',
               'Year 4, Sem 1',
               'Year 4, Sem 2',
               'Year 5, Sem 1 + Postbac']

# Need to change the axis to not be shared for ax6, or make a new scatter entirely
ax6.scatter(time_series, sem_avgs)

plt.show()
