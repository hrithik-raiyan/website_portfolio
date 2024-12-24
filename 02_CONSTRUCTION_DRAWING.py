import streamlit as st
from PIL import Image
from pathlib import Path

st.title("PROJECT 02_CONSTRUCTION DRAWING")
st.markdown('*<p style="color:grey; font-size:25px;">ARCH 314 | WORKING DRAWING | LEVEL 3, TERM 2 | JANUARY 2023</p>*', unsafe_allow_html=True)

# Add a custom styled divider
st.markdown("<hr style='border: 2px solid black;'/>", unsafe_allow_html=True)

# Base directory for image sources
BASE_DIR = Path(r"/mount/src/website_portfolio/_Source Images")

# List of image paths for each slider
image_paths_slider_1 = [
    BASE_DIR / "WD_1901027_RE_FLOOR AND WALL FINISH_Page_2.png",
    BASE_DIR / "WD_1901027_RE_FLOOR AND WALL FINISH_Page_1.png",
    BASE_DIR / "WD_1901027_RE_WALL LAYOUT_Page_4.png",
]

image_paths_slider_2 = [
    BASE_DIR / "WD_1901027_RE_FALSE SLAB AND LINTEL_Page_2.png",
    BASE_DIR / "WD_1901027_RE_FALSE SLAB AND LINTEL_Page_1.png",
    BASE_DIR / "WD_1901027_RE_FALSE SLAB AND LINTEL_Page_3.png",
]

image_paths_slider_3 = [
    BASE_DIR / "WD_1901027_RE_WALL LAYOUT_Page_2.png",
    BASE_DIR / "WD_1901027_RE_WALL LAYOUT_Page_3.png",
    BASE_DIR / "WD_1901027_RE_WALL LAYOUT_Page_6.png",
]

# Function to safely load images
def load_images(image_paths):
    valid_images = []
    for img_path in image_paths:
        if img_path.exists():
            try:
                valid_images.append(Image.open(img_path))
            except Exception as e:
                st.error(f"Failed to load image: {img_path} - {e}")
        else:
            st.warning(f"Image not found: {img_path}")
    return valid_images

# Load images with validation
images_slider_1 = load_images(image_paths_slider_1)
images_slider_2 = load_images(image_paths_slider_2)
images_slider_3 = load_images(image_paths_slider_3)

# Display images if valid
if images_slider_1 and images_slider_2 and images_slider_3:
    cols = st.columns(3)

    with cols[0]:
        selected_index_1 = st.slider("**Wall and Floor Finish**", 0, len(images_slider_1) - 1, 0)
        captions_slider_1 = ["Ground Floor", "First Floor", "Exploded View"]
        st.image(images_slider_1[selected_index_1], caption=captions_slider_1[selected_index_1], use_container_width=True)

    with cols[1]:
        selected_index_2 = st.slider("**Lintel and False Slab**", 0, len(images_slider_2) - 1, 0)
        captions_slider_2 = ["Ground Floor", "First Floor", "Exploded View"]
        st.image(images_slider_2[selected_index_2], caption=captions_slider_2[selected_index_2], use_container_width=True)

    with cols[2]:
        selected_index_3 = st.slider("**Wall Layout**", 0, len(images_slider_3) - 1, 0)
        captions_slider_3 = ["Ground Floor", "First Floor", "Exploded View"]
        st.image(images_slider_3[selected_index_3], caption=captions_slider_3[selected_index_3], use_container_width=True)
else:
    st.error("One or more image sliders could not load due to missing files. Please check the image paths.")

# Divider
st.markdown("<hr style='border: 2px solid orange;'/>", unsafe_allow_html=True)

# QR Code Section
st.markdown('**<p style="color:orange; font-size:25px;">WORKING DRAWING PORTFOLIO</p>**', unsafe_allow_html=True)
st.caption('*Here are hyperlinks and a QR code is added for interactive purposes.*')

# URL to be converted into a QR code
url = "https://drive.google.com/file/d/1oxqdaRxbv5et8CXhKhN-jjfQCu_IZwgd/view?usp=drive_link"

# Correct QR Code image path
qr_code_image_path = BASE_DIR / "_WD_QR CODE.png"

# QR Code Display
frame_size = 192
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

# Check if the QR code image exists
if qr_code_image_path.is_file():
    try:
        qr_image = Image.open(qr_code_image_path)
        st.image(qr_image, caption="Scan this QR code to open the link", width=frame_size)
    except Exception as e:
        st.error(f"Failed to load QR Code image: {qr_code_image_path} - {e}")
else:
    st.error(f"QR Code image not found at {qr_code_image_path}")

st.markdown("</div>", unsafe_allow_html=True)
st.write(f"*[Or click to view full Working Drawing book.]({url})*")

# Divider
st.markdown("<hr style='border: 2px solid black;'/>", unsafe_allow_html=True)
