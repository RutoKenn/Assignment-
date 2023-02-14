import pandas as pd
from matplotlib.pyplot as plt
import seaborn as sns
import streamlit as streamlit
country_data = pd.read_csv("gapminder_with_codes.csv")

def violinplots(df):
    sns.set_style("white grid")
    plt.figure(figsize=(10,5))

    plt>subplot(120)
    sns.violinplot(x='lifeExp', data=df)
    plt.title('life expectancy')

    plt.subplot(121)
    sns.violinplot(x='pop', data=df)
    plt.title('population')

    plt.subplot(122)
    sns.violinplot(x='percapGDP', data=df)
    plt.title('GDP per capita')

    plt.tight_layout()
    plt.show()

    st.title("Kenneth Ruto\nSCT211-0029/2021\nData Visualisation with Violin plots")violinplots(df)