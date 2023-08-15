import streamlit as st
from gtts import gTTS
from moviepy.editor import VideoClip, concatenate_videoclips
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

        # Generate image animation video
        image_duration = 5  # Adjust as needed
        image_clip = VideoClip(make_frame=lambda t: image_frame(image_path, t), duration=image_duration)

        # Load the audio clip
        audio_clip = AudioFileClip(tts_path)

        # Combine image and audio clips to create a final video clip
        final_clip = concatenate_videoclips([image_clip.set_audio(audio_clip)])

        # Write the video to a file
        video_path = os.path.join("uploads", "animated_video.mp4")
        final_clip.write_videofile(video_path, codec="libx264")

        st.video(video_path)

def image_frame(image_path, t):
    # This function returns the image frame at time t
    return ImageClip(image_path).get_frame(t)

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    main()
