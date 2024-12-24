# Save this as 'app.py' or run in Jupyter
import streamlit as st
from PIL import Image
import os

st.title("PROJECT 02_CONSTRUCTION DRAWING")
st.markdown('*<p style="color:grey; font-size:25px;">ARCH 314 | WORKING DRAWING | LEVEL 3, TERM 2 | JANUARY 2023</p>*', unsafe_allow_html=True)

# Add a custom styled divider
st.markdown(
    """
    <hr style="border: 2px solid black; border-width: 2px; font-weight: bold;"/>
    """, 
    unsafe_allow_html=True
)

# Header
st.markdown('**<p style="color:orange; font-size:25px;">WORKING DRAWING SHEETS</p>**', unsafe_allow_html=True)
st.caption('*Here are 3 set slides witch contains 3 drawings each*.')

# List of image paths (make sure you have at least 12 images)
image_paths = [
    r"_Source Images\_Workshop_Sheet 01.jpg",
    r"_Source Images\_Workshop_Sheet 02.jpg",
    r"_Source Images\_Workshop_Sheet 03.jpg",
    r"_Source Images\_Workshop_Sheet 04.jpg",
    r"_Source Images\_Workshop_Sheet 05.jpg",
    r"_Source Images\_Workshop_Sheet 06.jpg",
    r"_Source Images\_Workshop_Sheet 07.jpg",
    r"_Source Images\_Workshop_Sheet 08.jpg",
    r"_Source Images\_Workshop_Sheet 09.jpg",
    r"_Source Images\_Workshop_Sheet 10.jpg",
    r"_Source Images\_Workshop_Sheet 11.jpg",
    r"_Source Images\_Workshop_Sheet 12.jpg",
]


# List of image paths for each slider (ensure you have at least 3 images per slider)
image_paths_slider_1 = [
    r"_Source Images\WD_1901027_RE_FLOOR AND WALL FINISH_Page_2.png",
    r"_Source Images\WD_1901027_RE_FLOOR AND WALL FINISH_Page_1.png",
    r"_Source Images\WD_1901027_RE_WALL LAYOUT_Page_4.png",
]

image_paths_slider_2 = [
    r"_Source Images\WD_1901027_RE_FALSE SLAB AND LINTEL_Page_2.png",
    r"_Source Images\WD_1901027_RE_FALSE SLAB AND LINTEL_Page_1.png",
    r"_Source Images\WD_1901027_RE_FALSE SLAB AND LINTEL_Page_3.png",
]

image_paths_slider_3 = [
    r"_Source Images\WD_1901027_RE_WALL LAYOUT_Page_2.png",
    r"_Source Images\WD_1901027_RE_WALL LAYOUT_Page_3.png",
    r"_Source Images\WD_1901027_RE_WALL LAYOUT_Page_6.png",
]

# Load images for each slider
images_slider_1 = [Image.open(img) for img in image_paths_slider_1]
images_slider_2 = [Image.open(img) for img in image_paths_slider_2]
images_slider_3 = [Image.open(img) for img in image_paths_slider_3]

# Create 3 columns for the sliders and images
cols = st.columns(3)

# Slider for the first column
with cols[0]:
    selected_index_1 = st.slider("**Wall and Floor Finish** ", 0, len(images_slider_1) - 1, 0)
    captions_slider_1 = [
        "Ground Floor",
        "First Floor",
        "Exploded View"
    ]
    st.image(images_slider_1[selected_index_1], caption=captions_slider_1[selected_index_1], use_container_width=True)

# Slider for the second column
with cols[1]:
    selected_index_2 = st.slider("**Lintel and False slab**", 0, len(images_slider_2) - 1, 0)
    captions_slider_2 = [
        "Ground Floor",
        "First Floor",
        "Exploded View"
    ]
    st.image(images_slider_2[selected_index_2], caption=captions_slider_2[selected_index_2], use_container_width=True)

# Slider for the third column
with cols[2]:
    selected_index_3 = st.slider("**Wall Layout**", 0, len(images_slider_3) - 1, 0)
    captions_slider_3 = [
        "Ground Floor",
        "First Floor",
        "Exploded View"
    ]
    st.image(images_slider_3[selected_index_3], caption=captions_slider_3[selected_index_3], use_container_width=True)

# Add a custom styled divider
st.markdown(
    """
    <hr style="border: 2px solid orange; border-width: 2px; font-weight: bold;"/>
    """, 
    unsafe_allow_html=True
)

# Title
# Header
st.markdown('**<p style="color:orange; font-size:25px;">WORKING DRAWING PORTFOLIO</p>**', unsafe_allow_html=True)

st.caption('*Here are hyperlinks and a QR code is added for interactive purposes*.')

# URL to be converted into a QR code
url = "https://drive.google.com/file/d/1oxqdaRxbv5et8CXhKhN-jjfQCu_IZwgd/view?usp=drive_link"

# Provide the QR code image path directly
qr_code_image_path = r"D:\4-2\Algorithm\_Class Exercise\_11-17\_Streamlit\00\_Page Files\_WD_QR CODE.png"

# Set dimensions for 2-inch by 2-inch frame (approx. 192 pixels by 192 pixels for 96 DPI)
frame_size = 192

# Centered QR code
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if os.path.exists(qr_code_image_path):
    # Load and display the QR code image
    qr_image = Image.open(qr_code_image_path)
    st.image(qr_image, caption="Scan this QR code to open the link", width=frame_size)
else:
    st.error(f"QR Code image not found at {qr_code_image_path}")
st.markdown("</div>", unsafe_allow_html=True)

# Display the link as text
st.write(f"*[Or click to view full Working Drawing book.]({url})*")

# Add a custom styled divider
st.markdown(
    """
    <hr style="border: 2px solid black; border-width: 2px; font-weight: bold;"/>
    """, 
    unsafe_allow_html=True
)