# Reference doc - https://docs.streamlit.io/library/api-reference
import streamlit

streamlit.title("My Parent's New Healthy Diner")

streamlit.header("Breakfast Favorites")

streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-boiled free-range egg")
streamlit.text("🥑🍞 Avacado toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruits_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include
my_fruits_list = my_fruits_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruits_list.index), ['Avocado', 'Strawberries'])

fruits_to_show = my_fruits_list.loc[fruits_selected]  # for loc fun in pandas -  https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html 

streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")
#streamlit.text(fruityvice_response.json())

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)
