import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sb

import matplotlib.pyplot as plt

st.title('Football Player LaLiga 2018-2019 Stats')

file = pd.read_csv('./player_stats_laliga_18-19.csv')

dataframe = pd.DataFrame(data=file)

if st.checkbox('Montrer les données'):
    st.subheader("Caractéristiques et statistiques des joueurs")
    st.write(dataframe)
    
goal_slider = st.slider('Nombre de but à étudier')
st.write(goal_slider)

data_goal = pd.DataFrame(data=dataframe, columns= ["Goals scored"])
data_goal = data_goal[data_goal['Goals scored'] = 5 ]

st.line_chart(data_goal)
