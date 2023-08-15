import streamlit as st
from moviepy.editor import VideoClip
from gtts import gTTS
import os

def main():
    st.title("Audio Animation to Video")

    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3"])

    if uploaded_file:
        audio_path = os.path.join("uploads", uploaded_file.name)
        with open(audio_path, "wb") as f:
            f.write(uploaded_file.getvalue())

        text_content = convert_audio_to_text(audio_path)
        tts = gTTS(text=text_content, lang="en")
        tts_path = os.path.join("uploads", "tts.mp3")
        tts.save(tts_path)

        video_clip = VideoClip(make_frame=lambda t: [tts_path], duration=tts.duration)
        video_path = os.path.join("uploads", "animated_video.mp4")
        video_clip.write_videofile(video_path, codec="libx264")

        st.video(video_path)

def convert_audio_to_text(audio_path):
    # You would implement this function to convert audio to text
    # For this example, we'll return a dummy text
    return "This is a sample text generated from the audio."

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    main()

