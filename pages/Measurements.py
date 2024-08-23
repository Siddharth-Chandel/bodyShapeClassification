import streamlit as st
from utils.utitlity import load_css, shapeIdentifiyer
from PIL import Image
import time
from constants import updateResult

@st.experimental_dialog("Validation")
def confirmaton(measure:str, bust:float, waist:float, hip:float):
    """
    The function `confirmation` takes measurements for bust, waist, and hip, prompts the user to confirm
    the data input, processes the data, and writes the result to a file before switching to the result
    page.
    
    :param measure: The `measure` parameter in the `confirmation` function is a string that specifies
    the unit of measurement being used (e.g., 'CM' for centimeters)
    :type measure: str
    :param bust: The `bust` parameter typically refers to the measurement around the fullest part of the
    chest or bust. It is usually measured horizontally around the body
    :type bust: float
    :param waist: The `waist` parameter in the `confirmation` function refers to the measurement of the
    waist circumference. This parameter is a float type, which means it should be a decimal number
    representing the waist measurement in the specified unit of measurement (e.g., inches or
    centimeters)
    :type waist: float
    :param hip: The `hip` parameter in the `confirmation` function represents the measurement of the hip
    circumference. It is a floating-point number that indicates the size of the hips in inches or
    centimeters, depending on the `measure` parameter provided
    :type hip: float
    """
    st.write(f"Make sure you put the correct data in the context of <b><I><u>{measure}</u></I></b>.\nOtherwise, the result will be incorrect.", unsafe_allow_html=True)
    cols = st.columns(5)
    if cols[0].button("Submit"):
        with st.status("Processing"):
            time.sleep(4)
            if measure == 'CM':
                updateResult(shapeIdentifiyer(bust, waist, hip, measure))
            else:
                updateResult(shapeIdentifiyer(bust, waist, hip, measure))
                
        st.switch_page("pages/Result.py")
    if cols[1].button("Close"):
        st.experimental_rerun()

def app(page="measurements"):
    """
    The `app` function in Python sets up a web page for displaying measurements with input fields for
    shoulder, bust, waist, and hip sizes, allowing users to select units and calculate measurements.
    
    :param page: The `page` parameter in the `app` function is used to specify the page to be displayed. The default value is set to "measurements", defaults to measurements (optional)
    """
    st.set_page_config(page_icon="assests/MyStyle-logo.png",
                       page_title="Mystyle", layout="wide",initial_sidebar_state="collapsed")
    load_css(f"style/{page}.css")

    # The code snippet is setting up the layout for a web page using Streamlit in Python.
    # Here's a breakdown of what each part of the code is doing:
    with st.container():
        st.html("""<div id = 'main-container'></div>""")
        with st.container(border=False):
            st.html("""<div id = 'head-container'></div>""")
            cols = st.columns(2, gap="large", vertical_alignment="center")
            with cols[0]:
                sub_cols = st.columns(
                    [0.3, 1, 1, 1, 1], vertical_alignment='center')
                sub_cols[1].image("assests/MyStyle.png", width=250)
            with cols[1]:
                sub = st.columns([1, 1, 1, 0.5, 4, 1],
                                 vertical_alignment="center")
                sub[3].image("assests/search.png", width=20)
                sub[4].text_input(
                    "", label_visibility="collapsed", placeholder="search")
        
        # This part of the code sets up a section on the web page for inputting measurements
        st.html('''<h2 class="measures" ><u>Measurements</u></h2>''')
        img = Image.open("assests/measurements.webp")
        cols = st.columns([0.85,2,1])[1].image(img)
        cols = st.columns(6)
        with cols[2]:
            st.subheader("Bust Size")
            st.subheader("Waist Size")
            st.subheader("Hip Size")
        with cols[3]:
            bust = st.number_input("2",label_visibility="collapsed",placeholder=0, min_value=1.0, step=1.0, value=32.0)
            waist = st.number_input("3",label_visibility="collapsed",placeholder=0, min_value=1.0, step=1.0, value=32.0)
            hip = st.number_input("4",label_visibility="collapsed",placeholder=0, min_value=1.0, step=1.0, value=32.0)
        cols=st.columns([5,2,5])
        with cols[1]:
            selection = st.selectbox("1",label_visibility="collapsed",options=["Inches","CM"])
        
        if st.button("Calculate",type="primary"):
            confirmaton(selection, bust, waist, hip)
        st.header("## ")

if __name__ == "__main__":
    app()