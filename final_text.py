# import speech_recognition as sr
# from pydub import AudioSegment
# from pydub.silence import split_on_silence
# import tempfile
# import os

# recognizer = sr.Recognizer()

# def recognize_audio_segment(audio_file):
#     with sr.AudioFile(audio_file) as source:
#         audio = recognizer.record(source)
#         try:
#             text = recognizer.recognize_google(audio)
#             return text
#         except sr.UnknownValueError:
#             return "Recognition could not understand audio"
#         except sr.RequestError as e:
#             return f"Recognition request failed: {e}"

# audio_file = "sample_audio.wav"

# # Load the audio file using pydub
# audio = AudioSegment.from_wav(audio_file)

# # Split the audio into segments based on silence
# segments = split_on_silence(
#     audio,
#     min_silence_len=1000,  # Minimum silence length in milliseconds (adjust as needed)
#     silence_thresh=-32,    # Adjust this threshold for detecting silence
# )

# # Create a temporary directory to store audio segments
# temp_dir = tempfile.mkdtemp()

# for i, segment in enumerate(segments):
#     # Save each segment as a separate WAV file
#     segment_file = os.path.join(temp_dir, f"segment_{i}.wav")
#     segment.export(segment_file, format="wav")

#     # Recognize and print the transcribed text for each segment
#     text = recognize_audio_segment(segment_file)
#     print("Transcribed text (Segment {}):".format(i + 1), text)

# # Clean up temporary directory
# for segment_file in os.listdir(temp_dir):
#     os.remove(os.path.join(temp_dir, segment_file))
# os.rmdir(temp_dir)


### Above code is the whole code , next code removes the parts that are not recognized by the speech recognition module
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import tempfile
import os

recognizer = sr.Recognizer()

def recognize_audio_segment(audio_file):
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return None  # Return None when recognition fails

audio_file = "sample_audio.wav"

# Load the audio file using pydub
audio = AudioSegment.from_wav(audio_file)

# Split the audio into segments based on silence
segments = split_on_silence(
    audio,
    min_silence_len=3000,  # Minimum silence length in milliseconds (adjust as needed)
    silence_thresh=-32,    # Adjust this threshold for detecting silence
)

# Create a temporary directory to store audio segments
temp_dir = tempfile.mkdtemp()

# Create or open a Markdown file for writing
with open("output.md", "w", encoding="utf-8") as md_file:
    for i, segment in enumerate(segments):
        # Save each segment as a separate WAV file
        segment_file = os.path.join(temp_dir, f"segment_{i}.wav")
        segment.export(segment_file, format="wav")

        # Recognize and store the transcribed text for each segment (if successful)
        text = recognize_audio_segment(segment_file)
        if text is not None:
            md_file.write(f"### Transcribed text (Segment {i + 1}):\n")
            md_file.write(f"{text}\n\n")

# Clean up temporary directory
for segment_file in os.listdir(temp_dir):
    os.remove(os.path.join(temp_dir, segment_file))
os.rmdir(temp_dir)
