# Import python packages.
import streamlit as st
# from snowflake.snowpark.context import get_active_session

# Write directly to the app.
st.title("Customize your Smoothy orders! :cup_with_straw: {st.__version__}")
st.write(
  """Replace this example with your own code!
  **And if you're new to Streamlit,** check
  out our easy-to-follow guides at
  [docs.streamlit.io](https://docs.streamlit.io).
  """
)

#option = st.selectbox(
#    "How would you like to be contacted?",
#    ("Strawbwries", "Peaches", "Banana"),
#)
#st.write("You selected:", option)

# from snowflake.snowpark.functions import col

name_order = st.text_input("Name on Smootie", "")
st.write("The current name on Smootie is:", name_order)

# session = get_active_session()
# my_dataframe = session.table("smoothies.public.fruit_options").select (col('FRUIT_NAME'))
# #st.dataframe(data=my_dataframe, use_container_width=True)

# ingredients_list = st.multiselect('choose from the list:', my_dataframe)

if ingredients_list:
   # st.write(ingredients_list)
   # st.text(ingredients_list)

    ingredients_string = ''
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '
    
    st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients, name_on_order)
                    values ('""" + ingredients_string + """','""" + name_order + """')"""
    st.write(my_insert_stmt)
    #st.stop()
    
    time_to_insert = st.button('Insert Otem')
    # if time_to_insert:
    #    session.sql(my_insert_stmt).collect()
    #    st.success('Your Smoothie is ordered!', icon="✅")
    
