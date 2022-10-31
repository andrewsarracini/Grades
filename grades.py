from turtle import width
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# arr = np.array([[8, 3, 6, 0, 8, 6, 5, 4, 3, 6],
#                 [9, 10, 11, 11, 8, 9, 8, 8, 9, 3],
#                 [4, 8, 7, 8, 11, 7, 9, 11, 11],
#                 [6, 11, 10, 11, 11, 11, 11, 11],
#                 [11, 10, 11, 11],
#                 [11]]),

# df = pd.DataFrame(arr, columns=['First Year',
#                                 'Second Year',
#                                 'Third Year',
#                                 'Fourth Year',
#                                 'Fifth Year',
#                                 'Postbac'])

# print(df)

my_dict = {'First Year': [8, 3, 6, 0, 8, 6, 5, 4, 3, 6],
           'Second Year': [9, 10, 11, 11, 8, 9, 8, 8, 9, 3],
           'Third Year': [4, 8, 7, 8, 11, 7, 9, 11, 11],
           'Fourth Year': [6, 11, 10, 12, 12, 11, 11, 12],
           'Fifth Year': [12, 10, 11, 11],
           'Postbac': [12]}

grades_df = pd.DataFrame({key: pd.Series(value)
                         for key, value in my_dict.items()})

all_avg = grades_df.mean()
# fir_avg = grades_df['First Year'].mean()
# sec_avg = grades_df['Second Year'].mean()
# thir_avg = grades_df['Third Year'].mean()
# four_avg = grades_df['Fourth Year'].mean()
# fif_avg = grades_df['Fifth Year'].mean()

total_avg = (grades_df['First Year'].sum() + grades_df['Second Year'].sum() + grades_df['Third Year'].sum() +
             grades_df['Fourth Year'].sum() + grades_df['Fifth Year'].sum() + grades_df['Postbac'].sum()) / 42

''' Separating the data by semester'''
# Y1_sem1 = [8, 3, 6, 0, 8]
# Y1_sem2 = [6, 5, 4, 3, 6]
# Y2_sem1 = [9, 10, 11, 11, 8]
# Y2_sem2 = [9, 8, 8, 9, 3]
# Y3_sem1 = [4, 8, 7, 8, 11]
# Y3_sem2 = [7, 9, 11, 11]
# Y4_sem1 = [6, 11, 10, 12]
# Y4_sem2 = [12, 11, 11, 12]
# Y5_sem1 = [12, 10, 11, 11]

# fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6),
#       (ax7, ax8), (ax9, ax10)) = plt.subplots(5, 2, sharex=True, sharey=True)

''' Separating the data by academic year'''
fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, 1, sharex=True, sharey=True)

Y1 = [8, 3, 6, 0, 8, 6, 5, 4, 3, 6]
Y2 = [9, 10, 11, 11, 8, 9, 8, 8, 9, 3]
Y3 = [4, 8, 7, 8, 11, 7, 9, 11, 11, np.NaN]
Y4 = [6, 11, 10, 12, 12, 11, 11, 12, np.NaN, np.NaN]
Y5 = [12, 10, 11, 11, 12, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN]

'''Making a histogram'''
ax1.hist(Y1, width=0.75, edgecolor='k')
ax2.hist(Y2, width=0.75, edgecolor='k')
ax3.hist(Y3, width=0.75, edgecolor='k')
ax4.hist(Y4, width=0.75, edgecolor='k')
ax5.hist(Y5, width=0.75, edgecolor='k')

plt.show()
