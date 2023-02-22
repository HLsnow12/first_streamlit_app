# python libraries imported
import streamlit
import pandas
import requests

#streamlit.title ('My parents healthy Meal 🥣 ')
#streamlit.header('Breakfast Menu 🥗 ')
#streamlit.text('Omega 3 & Blueberry Oatmeal🥑🍞')
#streamlit.text('Kale, Spinach & Rocket Smoothie')
#streamlit.text('Hard-Boiled Free-Range Egg🐔')
 
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#reading file from csv
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#set index on column Fruit
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])


fruits_to_show = my_fruit_list.loc[fruits_selected]
#streamliting via dataframes
streamlit.dataframe(fruits_to_show)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
