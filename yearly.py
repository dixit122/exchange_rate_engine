import streamlit as st
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px


def yearly(x,curr2):


    df1=pd.read_csv("Exchange_Rate_Report_2012.csv")
    df2=pd.read_csv("Exchange_Rate_Report_2013.csv")
    df3=pd.read_csv("Exchange_Rate_Report_2014.csv")
    df4=pd.read_csv("Exchange_Rate_Report_2015.csv")
    df5=pd.read_csv("Exchange_Rate_Report_2016.csv")
    df6=pd.read_csv("Exchange_Rate_Report_2017.csv")
    df7=pd.read_csv("Exchange_Rate_Report_2018.csv")
    df8=pd.read_csv("Exchange_Rate_Report_2019.csv")
    df9=pd.read_csv("Exchange_Rate_Report_2020.csv")
    df10=pd.read_csv("Exchange_Rate_Report_2021.csv")
    df11=pd.read_csv("Exchange_Rate_Report_2022.csv")


    df1=df1.fillna(method="bfill")
    df2=df2.fillna(method="bfill")
    df3=df3.fillna(method="bfill")
    df4=df4.fillna(method="bfill")
    df5=df5.fillna(method="bfill")
    df6=df6.fillna(method="bfill")
    df7=df7.fillna(method="bfill")
    df8=df8.fillna(method="bfill")
    df9=df9.fillna(method="bfill")
    df10=df10.fillna(method="bfill")
    df11=df11.fillna(method="bfill")




    total=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11])

    total=total.fillna(method="bfill")
    df = {"2012": df1, "2013": df2, "2014": df3, "2015": df4, "2016": df5, "2017": df6, "2018": df7, "2019": df8,
          "2020": df9, "2021": df10, "2022": df11}
    data = df[x]

    temp = list(data[curr2])
    date = list(data['Date'])
    ma=date[temp.index(max(temp))]
    mi=date[temp.index(min(temp))]
    df=pd.DataFrame(temp,date)
    print(ma)
    fig=px.line(df)
    fig.update_xaxes(tickangle=270)
    fig.update_xaxes(title_text='Date')
    fig.update_yaxes(title_text='Exchange Rate')    
    st.write(fig)
    st.write("Highest on date:",ma,":",max(temp))
    st.write("Lowest on date:",mi,":",min(temp))

