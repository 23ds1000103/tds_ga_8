import streamlit as st
import pandas as pd

left_column, mid, right_column = st.columns([2,2,2])

mid.image('https://www.iitm.ac.in/themes/custom/iitm/assets/images/logo.png')
st.markdown(""" <p style="text-align: center; font-size: xx-large; font-weight: bold;
">Tools in Data Science</p> """, unsafe_allow_html=True)

st.markdown(""" <p style="text-align: center; font-size: x-large; font-weight: bold;
">Graded Assignment - 8</p> """, unsafe_allow_html=True)

if "submitted" not in st.session_state:
  st.session_state.submitted = False

if "confirmation" not in st.session_state:
  st.session_state.confirmation = False

def click_button():
  st.session_state.confirmation = True

def main():
  st.sidebar.write("#   Input area")
  with st.sidebar.form(key="Input_form"):
    num_1 = st.number_input("Enter the first number:")
    num_2 = st.number_input("Enter the second number:")
    num_3 = st.number_input("Enter the third number:")
    submitted = st.form_submit_button("Submit")
    
  if submitted:
    st.session_state.confirmation = False
    st.session_state.submitted = True
    st.info(f"""The values you have entered are:  
    Num1 = {num_1}   
    Num2 = {num_2}   
    Num3 = {num_3}.   
    """)
    st.warning(""" :triangular_flag_on_post:
    Please confirm if you want to proceed :triangular_flag_on_post:""")
    st.button("Confirm", on_click=click_button)
  
  if st.session_state.confirmation:
    st.balloons()
    st.success(":white_check_mark: Successfully submitted :sunglasses:")
    result = largest(num_1,num_2,num_3)
    st.subheader("Output")
    st.write(f"#### The largest of the three given numbers is: {result}")

def largest(num_1,num_2,num_3):
  result = num_1
  if num_2 > result:
    result = num_2
  if num_3 > result:
    result = num_3
  return(result)

main()




    




