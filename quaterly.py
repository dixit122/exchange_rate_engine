import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px
import streamlit as st

def quaterly(year,quater,curr2):
    df1 = pd.read_csv("Exchange_Rate_Report_2012.csv")
    df2 = pd.read_csv("Exchange_Rate_Report_2013.csv")
    df3 = pd.read_csv("Exchange_Rate_Report_2014.csv")
    df4 = pd.read_csv("Exchange_Rate_Report_2015.csv")
    df5 = pd.read_csv("Exchange_Rate_Report_2016.csv")
    df6 = pd.read_csv("Exchange_Rate_Report_2017.csv")
    df7 = pd.read_csv("Exchange_Rate_Report_2018.csv")
    df8 = pd.read_csv("Exchange_Rate_Report_2019.csv")
    df9 = pd.read_csv("Exchange_Rate_Report_2020.csv")
    df10 = pd.read_csv("Exchange_Rate_Report_2021.csv")
    df11 = pd.read_csv("Exchange_Rate_Report_2022.csv")

    df1 = df1.fillna(method="bfill")
    df2 = df2.fillna(method="bfill")
    df3 = df3.fillna(method="bfill")
    df4 = df4.fillna(method="bfill")
    df5 = df5.fillna(method="bfill")
    df6 = df6.fillna(method="bfill")
    df7 = df7.fillna(method="bfill")
    df8 = df8.fillna(method="bfill")
    df9 = df9.fillna(method="bfill")
    df10 = df10.fillna(method="bfill")
    df11 = df11.fillna(method="bfill")
    df = {"2012": df1, "2013": df2, "2014": df3, "2015": df4, "2016": df5, "2017": df6, "2018": df7, "2019": df8,
          "2020": df9, "2021": df10, "2022": df11}

    df = df[year]
    data=df[curr2]
    date=list(df['Date'])
    dataQ1=[]
    dateQ1=[]
    dataQ2=[]
    dateQ2=[]
    dataQ3=[]
    dateQ3=[]
    dataQ4=[]
    dateQ4=[]
    for i in range(len(date)):
        y=date[i].split("-")
        if y[1]=='Jan' or y[1]=='Feb' or y[1]=='Mar':
            dataQ1.append(data[i])
            dateQ1.append(date[i])
        elif y[1]=='Apr' or y[1]=='May' or y[1]=='Jun':
            dataQ2.append(data[i])
            dateQ2.append(date[i])
        elif y[1]=='Jul' or y[1]=='Aug' or y[1]=='Sep':
            dataQ3.append(data[i])
            dateQ3.append(date[i])
        else:
            dataQ4.append(data[i])
            dateQ4.append(date[i])

    if quater=='QUARTER 1':
        df=pd.DataFrame(dataQ1,dateQ1)
        ma=dateQ1[dataQ1.index(max(dataQ1))]
        mi=dateQ1[dataQ1.index(min(dataQ1))]
        fig = px.line(df)
        fig.update_xaxes(tickangle=270)
        fig.update_xaxes(title_text='Date')
        fig.update_yaxes(title_text='Exchange Rate')
        st.write(fig)
        st.write("Highest on date:",ma,":",max(dataQ1))
        st.write("Lowest on date:",mi,":",min(dataQ1))
    elif quater=='QUARTER 2':
        df=pd.DataFrame(dataQ2,dateQ2)
        ma=dateQ2[dataQ2.index(max(dataQ2))]
        mi=dateQ2[dataQ2.index(min(dataQ2))]
        fig = px.line(df)
        fig.update_xaxes(tickangle=270)
        fig.update_xaxes(title_text='Date')
        fig.update_yaxes(title_text='Exchange Rate')
        st.write(fig)
        st.write("Highest on date:",ma,":",max(dataQ2))
        st.write("Lowest on date:",mi,":",min(dataQ2))
    elif quater=='QUARTER 3':
        df=pd.DataFrame(dataQ3,dateQ3)
        ma=dateQ3[dataQ3.index(max(dataQ3))]
        mi=dateQ3[dataQ3.index(min(dataQ3))]
        fig = px.line(df)
        fig.update_xaxes(tickangle=270)
        fig.update_xaxes(title_text='Date')
        fig.update_yaxes(title_text='Exchange Rate')
        st.write(fig)
        st.write("Highest on date:",ma,":",max(dataQ3))
        st.write("Lowest on date:",mi,":",min(dataQ3))
    elif quater=='QUARTER 4':
        df=pd.DataFrame(dataQ4,dateQ4)
        ma=dateQ4[dataQ4.index(max(dataQ4))]
        mi=dateQ4[dataQ4.index(min(dataQ4))]
        fig = px.line(df)
        fig.update_xaxes(tickangle=270)
        fig.update_xaxes(title_text='Date')
        fig.update_yaxes(title_text='Exchange Rate')
        st.write(fig)
        st.write("Highest on date:",ma,":",max(dataQ4))
        st.write("Lowest on date:",mi,":",min(dataQ4))
    plt.show()



