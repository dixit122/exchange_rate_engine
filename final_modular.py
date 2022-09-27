#!/usr/bin/env python
# coding: utf-8

# In[4]:


from sqlite3 import Date
from tkinter import CURRENT
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
from yearly import yearly
from monthly import monthly
from quaterly import quaterly
from weekly import week


st.set_page_config(page_title="Currency Exchange Rate",page_icon=":dollar:")

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


st.header("WELCOME TO CURRENCY EXCHANGE ENGINE")
total=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11])

currency={}
valuesOfCurrency=['Algerian dinar   (DZD)                     ', 'Australian dollar   (AUD)                     ', 'Bahrain dinar   (BHD)                     ', 'Bolivar Fuerte   (VEF)                     ', 'Botswana pula   (BWP)                     ', 'Brazilian real   (BRL)                     ', 'Brunei dollar   (BND)                     ', 'Canadian dollar   (CAD)                     ', 'Chilean peso   (CLP)                     ', 'Chinese yuan   (CNY)                     ', 'Colombian peso   (COP)                     ', 'Czech koruna   (CZK)                     ', 'Danish krone   (DKK)                     ', 'Euro   (EUR)                     ', 'Hungarian forint   (HUF)                     ', 'Icelandic krona   (ISK)                     ', 'Indian rupee   (INR)                     ', 'Indonesian rupiah   (IDR)                     ', 'Iranian rial   (IRR)                     ', 'Israeli New Shekel   (ILS)                     ', 'Japanese yen   (JPY)                     ', 'Kazakhstani tenge   (KZT)                     ', 'Korean won   (KRW)                     ', 'Kuwaiti dinar   (KWD)                     ', 'Libyan dinar   (LYD)                     ', 'Malaysian ringgit   (MYR)                     ', 'Mauritian rupee   (MUR)                     ', 'Mexican peso   (MXN)                     ', 'Nepalese rupee   (NPR)                     ', 'New Zealand dollar   (NZD)                     ', 'Norwegian krone   (NOK)                     ', 'Omani rial   (OMR)                     ', 'Pakistani rupee   (PKR)                     ', 'Peruvian sol   (PEN)                     ', 'Philippine peso   (PHP)                     ', 'Polish zloty   (PLN)                     ', 'Qatari riyal   (QAR)                     ', 'Russian ruble   (RUB)                     ', 'Saudi Arabian riyal   (SAR)                     ', 'Singapore dollar   (SGD)                     ', 'South African rand   (ZAR)                     ', 'Sri Lankan rupee   (LKR)                     ', 'Swedish krona   (SEK)                     ', 'Swiss franc   (CHF)                     ', 'Thai baht   (THB)                     ', 'Trinidadian dollar   (TTD)                     ', 'Tunisian dinar   (TND)                     ', 'U.A.E. dirham   (AED)                     ', 'U.K. pound   (GBP)                     ', 'U.S. dollar   (USD)                     ', 'Uruguayan peso   (UYU)                     ']



k=0

y=list(df1.columns)
names=y[1:]
cname=list()
for i in names:
    i=i.strip(" ")
    cname.append(i)
    currency[i]=valuesOfCurrency[k]
    k=k+1


# st.write('CURRENCY 1: USD')
currency1={'USD':'USD'}
selected_currency1=st.selectbox("Select the type of Currency",currency1.keys())
selected_currency2=st.selectbox("Select the type of Currency",currency.keys())

flg=0
c1 = st.sidebar.selectbox("Currency 1",currency.keys())
amt = st.sidebar.number_input("Enter amount")
c2 = st.sidebar.selectbox("Currency 2",currency.keys())
c1_original = currency[c1]
c2_original = currency[c2]
cur1 = list(total[c1_original])
cur2 = list(total[c2_original])
dates = list(total['Date'])
period=st.sidebar.date_input("Select date of conversion ")
period_str = period.strftime("%d-%b-%y")
if period_str[0]=='0':
    period_str=period_str[1:]
for i in range(len(dates)):
    if(period_str==dates[i]):
        flg=1
        st.sidebar.write(str(amt)," ",c1," = ",str(amt*(cur2[i]/cur1[i]))," ",c2)
        break

if flg==0:
    st.sidebar.write("Data for this date not found!!")

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)

all_years={
    "2012":df1,
    "2013":df2,
    "2014":df3,
    "2015":df4,
    "2016":df5,
    "2017":df6,
    "2018":df7,
    "2019":df8,
    "2020":df9,
    "2021":df10,
    "2022":df11,
}

all_months={
    "Jan":"Jan",
    "Feb":"Feb",
    "Mar":"Mar",
    "Apr":"Apr",
    "May":"May",
    "Jun":"Jun",
    "Jul":"Jul",
    "Aug":"Aug",
    "Sept":"Sept",
    "Oct":"Oct",
    "Nov":"Nov",
    "Dec":"Dec"
}

all_weeks={
    '1':1,'2':2,'3':3,'4':4,'5':5
}



ques = st.radio("RANGE OF DATA",('ALL YEARS','YEARLY','MONTHLY','QUARTERLY','WEEKLY','DATE RANGE','FX CONVERTER'))
to_compare=currency[selected_currency2]
# df_to_plot=pd.DataFrame(total[to_compare].values)
list_years=(all_years.keys)
df_x=list(total['Date'].values)
if ques == 'ALL YEARS':
    df_to_plot=pd.DataFrame(list(total[to_compare].values),df_x)
    
    data=list(total[to_compare].values)
    fig = px.line(df_to_plot)
    fig.update_xaxes(tickangle=270)
    q=df_x[data.index(max(data))]
    p=df_x[data.index(min(data))]
    st.write(fig)
    st.write("Highest rate: ",max(data)," Date: ",q)
    st.write("Lowest rate:",min(data),"Date: ",p)
    

elif ques == 'YEARLY':
    selected_year=st.selectbox('SELECT THE YEAR', all_years)
    yearly(str(selected_year),to_compare)

elif ques == 'MONTHLY':
    selected_year=st.selectbox('SELECT THE YEAR', all_years)
    selected_month=st.selectbox('SELECT THE MONTH',all_months)
 
    monthly(str(selected_year),str(selected_month),to_compare)




elif ques == 'QUARTERLY':
    quarter=st.selectbox('SELECT THE QUARTER', ('QUARTER 1', 'QUARTER 2', 'QUARTER 3','QUARTER 4'))
    selected_year=st.selectbox('SELECT THE YEAR', all_years)
    
    quaterly(str(selected_year),str(quarter),to_compare)

elif ques == 'WEEKLY':
    selected_year=st.selectbox('SELECT THE YEAR', all_years)
    selected_month=st.selectbox('SELECT THE MONTH',all_months)
    selected_week=st.selectbox('SELECT THE WEEK',all_weeks.keys())

    week(str(selected_year),str(selected_month),str(selected_week),to_compare)
    


elif ques == 'DATE RANGE':
    start=st.date_input("Select the Start Date")
    end=st.date_input("Select the End Date")

    start=start.strftime("%d-%b-%Y")
    end=end.strftime("%d-%b-%Y")

    startString=start.split('-')
    if(startString[0][0]=='0'):
        startString[0]=startString[0][1:]
    
    startString[2]=startString[2][2:]
    start=startString[0]+'-'+startString[1]+'-'+startString[2]

    endString=end.split('-')
    if(endString[0][0]=='0'):
        endString[0]=endString[0][1:]
    
    endString[2]=endString[2][2:]
    end=endString[0]+'-'+endString[1]+'-'+endString[2]

    # print(start)
    # print(end)
    data=[]
    flag=0
    f1=0
    f2=0
    date=[]
    all_dates=list(total['Date'])
    all_values=list(total[currency[selected_currency2]])
    for i in range(len(total)):
        # print(start," ",all_dates[i])
        if(all_dates[i]==start):
            f1=1
        if(f2==1):
            break
        if(f1==1 and f2==0):
            if(all_dates[i]==end):
                print(end," ",all_dates[i])
                f2=1
            data.append(all_values[i])
            date.append(all_dates[i])

    # print(data)
    df_to_plot=pd.DataFrame(data,date)
    fig = px.line(df_to_plot)
    fig.update_xaxes(tickangle=270)
    if(len(data)>0):
        q=date[data.index(max(data))]
        p=date[data.index(min(data))]
        st.write(fig)
        st.write("Highest rate: ",max(data),"Date: ",q)
        st.write("Lowest rate:",min(data),"Date: ",p)
    else:
        st.write("Sorry, No Data Available for the selected dates.")
    # df=pd.DataFrame(temp,date)
            
elif ques=='FX CONVERTER':
    curr = currency[selected_currency2]
    data = []
    date = st.date_input('ENTER DATE')
    date=str(date)
    print(date)
    i=date.split("-")
    k=""

    if i[1]=='01':
        k='Jan'
    elif i[1]=='02':
        k='Feb'
    elif i[1]=='03':
        k='Mar'
    elif i[1]=='04':
        k='Apr'
    elif i[1]=='05':
        k='May'
    elif i[1]=='06':
        k='Jun'
    elif i[1]=='07':
        k='Jul'
    elif i[1]=='08':
        k='Aug'
    elif i[1]=='09':
        k='Sep'
    elif i[1]=='10':
        k='Oct'
    elif i[1]=='11':
        k='Nov'
    elif i[1]=='12':
        k='Dec'
    date=i[2]+"-"+k+"-"+i[0][2]+i[0][3]



    flag = 0
    f1 = 0
    y = list(df1.columns)
    names = y[1:]
    cname = list()
    for i in names:
        i = i.strip(" ")
        cname.append(i)

    for i in range(len(total)):
        a = total.iloc[i, 0]
        a = str(a)
        if date == a:
            val = total.iloc[i, :]
            val = val.tolist()
            val = val[1:]
            val.pop()
            f1 = 1
            break

    if f1 == 1:
        dd = pd.DataFrame({ 'CURRENCY':cname,'EXCHANGE RATE':val})
        dd=dd.dropna()
        st.write(dd)

    else:
        st.write("Sorry, No Data Available for the selected dates.")


# In[ ]:




