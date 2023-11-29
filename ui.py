import streamlit as st
from streamlit_option_menu import option_menu
import os
import base64
from PIL import Image
import cv2
from skimage.metrics import structural_similarity as ssim
import warnings
warnings.filterwarnings('ignore') 
st.set_page_config(layout="wide", page_title="Avatar_Generator")
def download_sample_obj(x):
    # Replace with the path to your sample .obj file
    
    sample_obj_path = x+".obj"

    with open(sample_obj_path, "rb") as file:
        obj_contents = file.read()

    obj_base64 = base64.b64encode(obj_contents).decode()
    href = f'data:application/octet-stream;base64,{obj_base64}'
    download_link = f'<a href="{href}" download="output_model.obj"><button style="background-color: #3498db; color: white; padding: 10px; border: none; border-radius: 5px;">Download Output File</button></a>'
    st.markdown(download_link, unsafe_allow_html=True)
# Function to download a sample video
def download_sample_video():
    sample_video_path = "female-1-casual.mp4"  # Replace with the path to your sample video file
    with open(sample_video_path, "rb") as file:
        video_contents = file.read()
    video_base64 = base64.b64encode(video_contents).decode()
    href = f'data:file/mp4;base64,{video_base64}'
    download_link = f'<a href="{href}" download="sample_video.mp4"><button style="background-color: #3498db; color: white; padding: 10px; border: none; border-radius: 5px;">Download Sample Video</button></a>'
    st.markdown(download_link, unsafe_allow_html=True)

def resize_image(image, target_shape):
    return cv2.resize(image, target_shape, interpolation=cv2.INTER_AREA)

def calculate_ssim(i1_path, i2_path):
    image1 = cv2.imread(i1_path, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(i2_path, cv2.IMREAD_GRAYSCALE)

    # Resize images to the same dimensions
    target_shape = (min(image1.shape[1], image2.shape[1]), min(image1.shape[0], image2.shape[0]))
    image1_resized = resize_image(image1, target_shape)
    image2_resized = resize_image(image2, target_shape)

    # Calculate SSIM
    ssim_score, _ = ssim(image1_resized, image2_resized, full=True)

    return round(ssim_score, 3)

# logo_image = "pesu-brand-identity.png"  # Replace with the path to your image file
# st.image(logo_image, use_container_width=True)
# logo_image = Image.open("pesu-brand-identity.png")
# st.sidebar.image(logo_image)
# st.sidebar.write("Dept. of CSE")

logo_image = Image.open("pesu-brand-identity.png")

# Center align the image and text in the sidebar
st.sidebar.image(logo_image, width = 100,caption=" ")

# Apply CSS to center the image and text
# st.sidebar.markdown(
#     """
#     <style>
#         div[data-testid="stSidebar"][role="presentation"] {
#             display: flex;
#             flex-direction: column;
#             align-items: center;
#             justify-content: center;
#             height: 100vh; /* Optional: Adjust the height as needed */
#         }
#         img {
#             max-width: 100%;
#             height: auto;
#             margin-bottom: 10px; /* Optional: Add margin between the image and text */
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
st.markdown(
    """
    <style>
        [data-testid=stSidebar] [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)

# Display the text
#st.sidebar.write("Dept. of CSE")

# Set up the sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", ["User guide", "Upload video or image", "Accuracy and Results"], 
        icons=['book', 'cloud-upload', 'clipboard-data'], menu_icon="cast", default_index=1)

# Display content based on the selected option on the main page
if selected == "User guide":
    # Add code for the "User guide" section on the main page
    st.write("# User Guide")
    #st.write("##We are planning to add description also here")
    st.write("#### Welcome to the User Guide! This guide will help you navigate and use our application effectively.")
    st.write("## Getting Started")
    st.write("#### 1. Choose the 'Upload video or Image' option to upload your video or image.")
    st.write("#### 2. You can also download a sample video to see the input format of the video to upload.")
    st.write("#### 3. You can download the output file generated as well by clicking on 'Download Output'")
    st.write("#### 4. Explore the 'Accuracy and Results' section to check the accuracy of your results.")
    st.write("## Additional Information")
    st.write("#### For any assistance, please contact the support team")
elif selected == "Upload video or image":
    # Add code for the "Upload video" section on the main page
    


    original_title = '<p style="font-family:Luminari; color:Black; font-size: 50px; text-align: center;">Welcome to Avatar Generator !!</p>'
    sub_title = '<p style="font-family:Brush Script MT; color:Black; font-size: 40px; text-align: center">Upload a video or image and get your personalized avatars in no time<p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.markdown(sub_title, unsafe_allow_html=True)
    #st.write("Upload your video here.")
    uploaded_file = st.file_uploader(" ", type=["png", "jpg", "jpeg","mov","avi","mp4"])

    if uploaded_file:
        #st.video(uploaded_file)
        file_name = uploaded_file.name
        file_name_without_extension = os.path.splitext(file_name)[0]
        # st.write(f"File Name: {file_name}")
        download_sample_obj(file_name_without_extension)
        # # Get the type of the file
        # file_type = uploaded_file.type
        # st.write(f"File Type: {file_type}")

    download_sample_video()
    #Take a video use it in python code. Need to add button after clicking that python code will run or colab will launch
elif selected == "Accuracy and Results":
    # Add code for the "Accuracy" section on the main page
    ground_truth_img_path=['man_front_img.jpeg','backimage_ground_truth.jpeg','woman_in_saree_gt.jpg','man-in-dhoti-kurta.png']
    output_img_path=['man_front_img_output.jpeg','backimage_model.jpeg','woman_in_saree_out.jpg','Man_in_dhoti_kurta_output.png']
    headings=['Front View','Back View', 'Front View of Woman in Saree','Front view of Man in Kurta']
    target_shape=(500,600)
    st.write("<h2 style='text-align: center;'>Accuracy of the model calculated using SSIM</h3>", unsafe_allow_html=True)
    for i in range(len(ground_truth_img_path)):
        st.write("<h3 style='text-align: center;'>{}</h3>".format(headings[i]), unsafe_allow_html=True)
        image1 = cv2.imread(ground_truth_img_path[i])
        image2 = cv2.imread(output_img_path[i])
        ssim_score1 = calculate_ssim(ground_truth_img_path[i], output_img_path[i])
        image1_resized = resize_image(image1, target_shape)
        image2_resized = resize_image(image2, target_shape)
        col1,col2=st.columns(2)
        # Resize images to the same dimensions
        # target_shape = (min(image1.shape[1], image2.shape[1]), min(image1.shape[0], image2.shape[0]))
        # image1_resized_ = resize_image(image1, target_shape)
        # image2_resized_ = resize_image(image2, target_shape)

        # # Calculate SSIM
        # ssim_score, _ = ssim(image1_resized_, image2_resized_, full=True)
        # ssim_score=round(ssim_score,3)

        with col1:
        #st.write("<h3 style='text-align: center;'>Front View</h3>", unsafe_allow_html=True)
            st.write("<h4 style='text-align: center;'>Ground Truth Image</h4>", unsafe_allow_html=True)
            st.image(image1_resized, width=475)
            st.write("<h4 style='text-align: center;'>SSIM Score: {}</h4>".format(ssim_score1), unsafe_allow_html=True)

            

        with col2:
            #st.write("<h3 style='text-align: center;'>Front View</h3>", unsafe_allow_html=True)
            st.write("<h4 style='text-align: center;'>Model Output Image</h4>", unsafe_allow_html=True)
            st.image(image2_resized,width=475)
            st.write("<h4 style='text-align: center;'>Accuracy: {}%</h4>".format(round(ssim_score1*100,2)), unsafe_allow_html=True)


