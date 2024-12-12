import streamlit as st
from utils.speech_to_text import speech_to_text_from_mic
from utils.text_to_image import text_to_image
import os
import time

st.set_page_config(page_title="Speech to Image Generator", page_icon="🖼️", layout="centered")

st.title("Speech to Image Generator")
st.subheader("Convert your speech or text into images using AI!")

st.markdown("""
    **How it works:**
    1. 🎙️ Click the button below to speak into your microphone.
    2. 📝 The system will convert your speech into text.
    3. 🖼️ Based on the text, an image will be generated and displayed here!
    4. You can also manually enter a description to generate an image.
""")

st.markdown("---")

# Track the progress of speech-to-text and image generation
speech_recognition_complete = False
image_generation_complete = False

st.header("Option 1: Generate Image from Speech")
st.write("Click the button to start speaking into the microphone.")

if st.button("🎤 Start Listening"):
    
    speech_bar = st.progress(0)
    speech_recognition_complete = False
    image_generation_complete = False

    with st.spinner("Listening... Please speak now..."):
        try:
            for i in range(1, 101):
                speech_bar.progress(i)
                time.sleep(0.03)  
            text = speech_to_text_from_mic()

            if text:
                speech_recognition_complete = True
                st.success("✅ Speech recognized successfully!")
                st.write(f"Recognized Text: {text}")
                speech_bar.progress(100)

                with st.spinner("Generating Image... Please wait..."):
                    image_bar = st.progress(0)

                   
                    for i in range(1, 101):
                        image_bar.progress(i)
                        time.sleep(0.03)  
                    output_image_path = text_to_image(text)

                    st.image(output_image_path, caption="Generated Image", use_container_width=True)
                    st.success("Image generated successfully!")
                    image_generation_complete = True
                    image_bar.progress(100)

            else:
                st.error("❌ Failed to recognize speech. Please try again.")
                speech_bar.progress(0)
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
            st.write("Please try again or check your microphone settings.")

st.header("Option 2: Generate Image from Text")
text_input = st.text_input("📝 Enter a description for the image:")
if text_input:
    with st.spinner("Generating Image..."):
        try:
            output_image_path = text_to_image(text_input)

            st.image(output_image_path, caption="Generated Image", use_container_width=True)
            st.success("Image generated successfully!")
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
            st.write("Please try again with a different description.")

if 'output_image_path' in locals():
    st.header("Download Generated Image")
    with open(output_image_path, "rb") as file:
        st.download_button(label="Download Image", data=file, file_name="generated_image.png", mime="image/png")



st.markdown("---")
st.markdown("""
    Built with ❤️ by Jyoti & Mamta | Powered by [Stable Diffusion AI](https://huggingface.co/CompVis/stable-diffusion-v-1-4-original)
""")
