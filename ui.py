import streamlit as st
from streamlit_option_menu import option_menu
import os
import base64
from PIL import Image
# Function to download a sample video
def download_sample_video():
    sample_video_path = "female-1-casual.mp4"  # Replace with the path to your sample video file
    with open(sample_video_path, "rb") as file:
        video_contents = file.read()
    video_base64 = base64.b64encode(video_contents).decode()
    href = f'data:file/mp4;base64,{video_base64}'
    download_link = f'<a href="{href}" download="sample_video.mp4"><button style="background-color: #3498db; color: white; padding: 10px; border: none; border-radius: 5px;">Download Sample Video</button></a>'
    st.markdown(download_link, unsafe_allow_html=True)

# logo_image = "pesu-brand-identity.png"  # Replace with the path to your image file
# st.image(logo_image, use_container_width=True)
logo_image = Image.open("pesu-brand-identity.png")
st.sidebar.image(logo_image)
st.sidebar.write("Dept. of CSE")
# Set up the sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", ["User guide", "Upload video", "Accuracy and Results", "About project"], 
        icons=['book', 'cloud-upload', 'clipboard-data', 'info-circle'], menu_icon="cast", default_index=1)

# Display content based on the selected option on the main page
if selected == "User guide":
    # Add code for the "User guide" section on the main page
    st.write("# User Guide")
    st.write("##We are planning to add description also here")
    st.write("Welcome to the User Guide! This guide will help you navigate and use our application effectively.")
    st.write("## Getting Started")
    st.write("1. Choose the 'Upload video' option to upload your video.")
    st.write("2. Explore the 'Accuracy' section to check the accuracy of your results.")
    st.write("3. View the 'Results' section for detailed analysis and outcomes.")
    st.write("## Additional Information")
    st.write("For any assistance, please refer to the documentation or contact our support team.")
elif selected == "Upload video":
    # Add code for the "Upload video" section on the main page
    st.write("Upload your video here.")
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])
    if uploaded_file:
        st.video(uploaded_file)
    download_sample_video()
    #Take a video use it in python code. Need to add button after clicking that python code will run or colab will launch
elif selected == "Accuracy and Results":
    # Add code for the "Accuracy" section on the main page
    st.write("Check the accuracy here.")
elif selected == "About project":
    # Add code for the "Results" section on the main page
    st.write("Project, paper link, dataset link.")

