# python libraries imported
import streamlit
import pandas

#streamlit.title ('My parents healthy Meal 🥣 ')
#streamlit.header('Breakfast Menu 🥗 ')
#streamlit.text('Omega 3 & Blueberry Oatmeal🥑🍞')
#streamlit.text('Kale, Spinach & Rocket Smoothie')
#streamlit.text('Hard-Boiled Free-Range Egg🐔')
 
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#reading file from csv
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#picklist option for fruits.
streamlist.multiselect("Pick some fruits:", list(my_fruit_list.index))

#streamlitting via dataframes
streamlit.dataframe(my_fruit_list)
