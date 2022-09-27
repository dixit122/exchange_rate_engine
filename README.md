# **Exchange Rate Engine**
## **An exchange rate engine created using streamlit library in python.**



# Functions implemented
- Read and store the data from file. 

- Create a use interface which allows users to select currency and desired duration. Users should have the ability to switch between weekly, monthly, quarterly, and annual charts

- Fetch data for given currency and time duration. Show the trend over a given period. Also display the date on which the rate was highest with the actual rate and date on which the rate was lowest along with the rate

- UI should have the option to select 2 currencies (Currency 1 and Currency 2). Currency 1 auto populate with USD. Users should have the search capability to search for a currency in currency 2 field. Display currency name next to currency field 

- Users should have an option to select the year for which they would prefer to see the data and graphs

- Provide a Service/Component which will provide FX rates for all currencies considering a base currency. For instance, USD as a base currency and value of all other currencies in terms of USD for a given date

- Provide a Service/Component to convert value of currency into another currency. For instance, if the user provides base currency as USD and target currency as INR and amount of 1000 and let’s say exchange rate is 79, component should convert amount into target currency and result should be 79,000 INR

- Provide option to select currency-1 also as any currency rather than populating it as USD always. Use USD as through currency and derive exchange rate between 2 currencies. For instance, if Sterling (GBP) and Australian Dollar (AUD) are the 2 currencies selected then derive direct exchange rate between GBP and USD. Once exchange rate is derived between GBP and USD currency, use that as base to derive value for second currency which is AUD in this example.


# Installation of Required Libraries
### The system should have python/Anaconda installed in the system.

## Link to download python:
> https://www.python.org/downloads/

## To install the required libraries, type the following commands in the command prompt.

## Streamlit
> pip install streamlit

## Numpy
> pip install numpy

## Plotly
> pip install plotly

## Pandas
> pip install pandas

# How to run the project
To run the project, open command prompt in the folder containing all the files of the project.

Type the following command in the command prompt.
> streamlit run final_modular.py
