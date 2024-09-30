import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

st.title("Titanic App by Guo Qian")

# read csv and show the dataframe
df = pd.read_csv('test.csv')
df

# create a figure with three subplots, size should be (15, 5)
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below

for i, cls in enumerate(sorted(df['Pclass'].unique()), start=0):
    axs[i].boxplot(df[df['Pclass'] == cls]['Fare'].dropna(), patch_artist=True)
    axs[i].set_title(f'Box Plot of Ticket Prices for Class {cls}')
    axs[i].set_xlabel('Class ' + str(cls))
    axs[i].set_ylabel('Ticket Price ($)')
plt.tight_layout()
st.pyplot(fig)
