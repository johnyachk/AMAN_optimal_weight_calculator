import numpy as np
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression


import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from PIL import Image
from sklearn.metrics import accuracy_score


st.header("Optimal Weight Calculator at AMAN Hospital")
st.subheader("Sirine Abou El Hasan")
st.subheader("B.J Devine formula")
selectb= st.sidebar.selectbox('Gender',["Male",'Female'])
slider1=st.sidebar.slider('Weight in Kg',45.5,150.0)
slider2=st.sidebar.slider('Height',1.50,2.20)


button=st.button('Get your optimal weight')
if button:
    if selectb=='Male' and slider1 and slider2:
        optimal_male_weight= ((((slider2 - 1.5) / 0.0254 )*2.3) + 50)
        optimal_male_weight=round(optimal_male_weight)
        over_under= slider1 - optimal_male_weight
        st.markdown(f"Your optimal weight is {optimal_male_weight} Kg ")
        if slider1 > optimal_male_weight:
            diff= round(slider1 - optimal_male_weight)
            st.markdown(f" You are over the optimal weight by around {diff} kg")
        else:
            diff1= round(optimal_male_weight - slider1)
            st.markdown(f" You are under the optimal weight by around {diff1} kg")
    else:
        #selectb=="Female" and slider1 and slider2
        optimal_female_weight = ((((slider2 - 1.5) / 0.0254) * 2.3) + 45.5)
        optimal_female_weight = round(optimal_female_weight)
        over_under = slider1 - optimal_female_weight
        st.markdown(f"Your optimal weight is {optimal_female_weight} Kg ")
        if slider1 > optimal_female_weight:
            diff = round(slider1 - optimal_female_weight)
            st.markdown(f" You are over the optimal weight by around {diff} kg")
        else:
            diff1 = round(optimal_female_weight - slider1)
            st.markdown(f" You are under the optimal weight by around {diff1} kg")















