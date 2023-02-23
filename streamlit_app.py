# python libraries imported
import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError

#streamlit.title ('My parents healthy Meal 🥣 ')
#streamlit.header('Breakfast Menu 🥗 ')
#streamlit.text('Omega 3 & Blueberry Oatmeal🥑🍞')
#streamlit.text('Kale, Spinach & Rocket Smoothie')
#streamlit.text('Hard-Boiled Free-Range Egg🐔')
 
#streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#reading file from csv
#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#set index on column Fruit
#my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
#fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])


#fruits_to_show = my_fruit_list.loc[fruits_selected]
#streamliting via dataframes
#streamlit.dataframe(fruits_to_show)

#streamlit.header('New section to display Streamlit response')
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#streamlit.text(fruityvice_response.json())
# write your own comment -what does the next line do? 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
#streamlit.dataframe(fruityvice_normalized)

#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#streamlit.write('The user entered ', fruit_choice)
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
#streamlit.dataframe(fruityvice_normalized)

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("select * from fruit_load_list")
#my_cur.execute ("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit test'));
#my_data_row = my_cur.fetchall()
#streamlit.text("Fruit Load List contains")
#streamlit.dataframe(my_data_row)

#add_my_fruit = streamlit.text_input('What fruit would you like information about?','Jackfruit')
#streamlit.write('The user entered ', add_my_fruit)

streamlit.header('Fruityvice Fruity Advice')
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
     streamlit.error("Please select a fruit")
   else:
     fruityviceresponse = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
     streamlit.dataframe(fruityvice_normalized)
except URL_Error as e:
   streamlit.error()
