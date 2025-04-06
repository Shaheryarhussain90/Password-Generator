import streamlit as st
import random
import string




def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters                      # include a to z and A to z

    if use_digits:
        characters += string.digits  # add number 0 to 9 agr user select kiya to

        if use_special:
            characters += string.punctuation  # @, #, !, $, &, *   special characters
    return " ".join(random.choice(characters) for _ in range(length))


# st.markdown(
    
#     """
#     <style>
#    .stApp{
#      background-color: black;
#     color: white;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )


st.title("password Grenrator")
length = st.slider("select password lengt", min_value=6, max_value=32, value=12)

use_digits = st.checkbox("Include Digit")

use_special = st.checkbox("Include special characters")

if st.button("Generae Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password:`{password}`")

    st.write("---------------------------------------------------------------")



    st.write("Build by Shaheryar Hussain")