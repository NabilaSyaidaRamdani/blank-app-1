import streamlit as st

st.title("Welcome to My Streamlit App!")

st.header('HI! Our Dear Customer')

st.subheader('Please fill Your Name')

Name = st.text_input(label='Full Name', value='')

City = st.text_input(label='City', value='')

State = st.text_input(label='State', value='')
 
with st.sidebar:
    
    st.text('Ini merupakan sidebar')
    
    values = st.slider(
        label='Select a range of values',
        min_value=0, max_value=100, value=(0, 100)
    )
    st.write('Values:', values)
    
import streamlit as st
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://i.pinimg.com/564x/ed/6b/be/ed6bbe5838979e5bca84c998cd2a87e6.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if st.button("Sign In"):
    st.write("You clicked on Sign In!")
    # Tambahkan logika untuk proses Sign In di sini

# Tombol Sign Up
if st.button("Sign Up"):
    st.write("You clicked on Sign Up!")
    # Tambahkan logika untuk proses Sign Up di sini
