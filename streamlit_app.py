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
streamlit.dataframe(my_fruits_list)

# Let's put a pick list here so they can pick the fruit they want to include
streamlit.multipicker(f"Pick some fruits: {list(my_fruits_list.index)}")