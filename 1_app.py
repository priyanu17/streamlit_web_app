import time
from PIL import Image
import streamlit as st

# title
st.title("Streamlit Title Text")

# header
st.header("Header text")

# subheader
st.subheader("Subheader text")

# text
st.text("This is normal text content")

# markdown
st.markdown("### Markdown text")

# different text colors
st.success("Successful text (appears in green)")
st.info("Information text (appers in blue)")
st.warning("Warning text (appers in yellow)")
st.error("Error text (appers in red)")

# streamlit exceptions
st.exception("Exceptions can usually extract stack trace of any exception")

# st.help(-> gets docs of any python fuction or feature)
st.help(str)
st.help(range)
st.help(int)

# streamlit write super function
st.write("write() super function command")
st.write(range(1, 100))

# working with images
img_1 = Image.open("Images/image_1.jfif")
st.image(img_1, width=500, caption="Image : 1 caption")

# working with videos
vid_1 = open("Videos/video_1.mp4", "rb").read()
st.video(vid_1)

# audio file
# audio_1 = open("Audios/audio_1.mp3", "rb").read()
# st.audio(audio_1, format="audio/mp3")

# Widgets (Checkbox)
if st.checkbox("Select/Unselect"):
    st.text("Check box : Selected")
else:
    st.text("Check box : NOT Selected")

# Widgets (Radio Buttons)
status = st.radio("Plese select your status:", ("Active", "Inactive", "Other"))

if status == "Active":
    st.success("Status : Active")
elif status == "Inactive":
    st.warning("Status : Inactive")
else:
    st.error("Invalid status value!!")

# selectbox
gender = st.selectbox("Please select your gender:",
                      ("Male", "Female", "Other"))

st.write("Selected gender : " + str(gender))

# multiselect
locations = st.multiselect("Select your preferred locations", (
    "Delhi", "Noida", "Gurugram", "Bangalore", "Hyderabad", "Mumbai", "Chennai", "Kolkata"))

if locations == []:
    locations = "No location is selected"
    st.write(locations)
else:
    st.write("Selected locations are : " + str(locations))

# sliders
rating = st.slider("Select rating from 1 to 10 : ", 1, 10)
st.write("Selected rating : " + str(rating))

# buttons
simple_button = st.button("Simple button (no functionality)")

if st.button("Button with function"):
    st.text("Display about information here")

# json content
st.text("Display formatted json content below")
st.json({"first": "Anu", "last": "Priya", "age": "24"})

# display raw code
st.text("Display raw code")
st.code("import numpy as np")

# Display raw code in chunk
with st.echo():
    import numpy as np
    import pandas as pd
    print("Hello World")

    def function_name():
        print("Inside function")
    # comments also displayed

# Progress Bar
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p+1)

# Spinner
st.text("Spinner content below")
with st.spinner("Waiting.."):
    time.sleep(3)
st.success("Finished")

# st.balloons()

# side bars
st.sidebar.header("About")
st.sidebar.text("Side bar content ")
