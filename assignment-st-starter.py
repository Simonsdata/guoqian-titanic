# import packages
import pandas as pd
import matplotlib.pyplot as plt

# show the title
print("Titanic App by Guo Qian")

# read csv and show the dataframe
df = pd.read_csv('test.csv')
print(df)

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
for i, cls in enumerate(sorted(df['Pclass'].unique()), start=0):
    axs[i].boxplot(df[df['Pclass'] == cls]['Fare'].dropna(), patch_artist=True)
    axs[i].set_title(f'Box Plot of Ticket Prices for Class {cls}')
    axs[i].set_xlabel('Class ' + str(cls))
    axs[i].set_ylabel('Ticket Price ($)')
plt.tight_layout()
plt.show()