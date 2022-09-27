#!/usr/bin/env python
# coding: utf-8

# In[54]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
  
def week(year,month,week,cur):
    
    df1 = pd.read_csv('Exchange_Rate_Report_2012.csv')
    df2 = pd.read_csv('Exchange_Rate_Report_2013.csv')
    df3 = pd.read_csv('Exchange_Rate_Report_2014.csv')
    df4 = pd.read_csv('Exchange_Rate_Report_2015.csv')
    df5 = pd.read_csv('Exchange_Rate_Report_2016.csv')
    df6 = pd.read_csv('Exchange_Rate_Report_2017.csv')
    df7 = pd.read_csv('Exchange_Rate_Report_2018.csv')
    df8 = pd.read_csv('Exchange_Rate_Report_2019.csv')
    df9 = pd.read_csv('Exchange_Rate_Report_2020.csv')
    df10 = pd.read_csv('Exchange_Rate_Report_2021.csv')
    df11 = pd.read_csv('Exchange_Rate_Report_2022.csv')

    df_all = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11],axis=0)
    
    df=pd.DataFrame()
    
    if year=='2012':
        df = df1
    if year=='2013':
        df = df2
    if year=='2014':
        df = df3
    if year=='2015':
        df = df4
    if year=='2016':
        df = df5
    if year=='2017':
        df = df6
    if year=='2018':
        df = df7
    if year=='2019':
        df = df8
    if year=='2020':
        df = df9
    if year=='2021':
        df = df10
    if year=='2022':
        df = df11
    x=[]
    y=[]
    
    temp=[]
    date = list(df['Date'])
    data = list(df[cur])
    for i in range(len(date)):
        d = str(date[i])
        a=d.split("-")
        if a[1]==month:
            if (int(week)-1)*7<int(a[0])<=int(week)*7 :
                x.append(a[0])
                y.append(data[i])
    
    ma=x[y.index(max(y))]
    mi=x[y.index(min(y))]
    df_to_plot=pd.DataFrame(y,x)
    
    fig = px.line(df_to_plot)
    fig.update_xaxes(title_text='Date')
    fig.update_yaxes(title_text='Exchange Rate')
    st.write(fig)
    st.write("Highest on date:",ma,"-",month,"-",year,":",max(y))
    st.write("Lowest on date:",mi,"-",month,"-",year,":",min(y))

# In[ ]:




