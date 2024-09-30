import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

st.title("Titanic App by Guo Qian")

# read csv and show the dataframe
df = pd.read_csv('train.csv')
df

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below

fig, ax = plt.subplots(1, 3,figsize=(15, 5))
classes = df['Pclass'].unique()
for i, pclass in enumerate(sorted(classes)):
    # 选择当前 Pclass 的数据
    data = df[df['Pclass'] == pclass]['Fare']
    ax[i].boxplot(data, patch_artist=True)
ax[0].set_ylabel('Fare')
ax[0].set_xlabel('Pclass = 1')
ax[1].set_xlabel('Pclass = 2')
ax[2].set_xlabel('Pclass = 3')
st.pyplot(fig)
