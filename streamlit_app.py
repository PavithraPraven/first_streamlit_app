import streamlit

streamlit.title('My Moms new healthy dinner')

streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 & Blueberry meal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avacoda Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.text_input("Pick some fruits:", 'cantaloupe')
streamlit.write(fruit_choice)
my_cur.execute("insert into fruit_load_list values('from streamlit')")

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Orange')
streamlit.write('The user entered ', fruit_choice)
my_cur.execute("insert into fruit_load_list values('from streamlit')")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# Normalization 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Display the results in table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

# Allow end user to add a fruit to a list
add_my_fruit = streamlit.text_input('What fruit would you like to add?','cantaloupe')
streamlit.write('Thanks for adding ', add_my_fruit)

my_cur.execute("insert into fruit_load_list values('from streamlit')")
