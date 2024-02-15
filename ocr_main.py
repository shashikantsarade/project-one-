!pip install pytesseract    
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
from PIL import Image
import pytesseract

# Set Tesseract path (change it as per your system configuration)
#pytesseract.pytesseract.tesseract_cmd = r'<path_to_tesseract_executable>'

def ocr_text(image):
    # Perform OCR on the image
    text = pytesseract.image_to_string(image)
    return text

def main():
    st.title("Image OCR App")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Perform OCR and display extracted text
        if st.button('Extract Text'):
            text = ocr_text(image)
            st.write('Extracted Text:', text)

if __name__ == '__main__':
    main()
