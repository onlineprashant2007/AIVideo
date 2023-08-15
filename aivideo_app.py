import streamlit as st
from gtts import gTTS
from moviepy.editor import VideoClip, AudioFileClip
from PIL import Image
import os

def main():
    st.title("Image Animation with Custom Text")

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png"])
    custom_text = st.text_input("Enter your custom text:")
    
    if uploaded_image and custom_text:
        # Process the uploaded image
        image_path = os.path.join("uploads", uploaded_image.name)
        with open(image_path, "wb") as f:
            f.write(uploaded_image.getvalue())

        # Convert custom text to speech
        tts = gTTS(text=custom_text, lang="en")
        tts_path = os.path.join("uploads", "tts.mp3")
        tts.save(tts_path)

        # Load the image and create an image clip
        image = Image.open(image_path)
        image_clip = ImageClip(image, duration=tts.duration)

        # Load the audio and create an audio clip
        audio_clip = AudioFileClip(tts_path)

        # Combine image and audio clips to create a video clip
        video_clip = image_clip.set_audio(audio_clip)

        # Write the video to a file
        video_path = os.path.join("uploads", "animated_video.mp4")
        video_clip.write_videofile(video_path, codec="libx264")

        st.video(video_path)

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    main()
