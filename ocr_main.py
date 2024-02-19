import streamlit as st
from PIL import Image
import easyocr

# Initialize the EasyOCR reader with automatic language detection
reader = easyocr.Reader(['en', 'hi', 'mr'])

def ocr_text(image):
    # Perform OCR on the image
    result = reader.readtext(image)
    # Extract text from the result
    text = ' '.join([text for _, text, _ in result])
    # Get the detected language
    languages = [lang for _, _, lang in result]
    detected_language = ', '.join(set(languages))  # Set to remove duplicates
    return text, detected_language

def main():
    st.title("   OCR अँप   ")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Perform OCR and display extracted text
        if st.button(' माहिती पहा '):
            with st.spinner('Performing OCR...'):
                text, detected_language = ocr_text(image)
                st.success('OCR Completed!')

                # Display detected language
                st.write(f"Detected Language(s): {detected_language}")

                # Display the extracted text in a box
                st.info('Extracted Text:')
                st.text_area(label='', value=text, height=200, max_chars=None)

if __name__ == '__main__':
    main()
