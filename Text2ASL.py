import os
import ipywidgets as widgets
from IPython.display import display, HTML
import time

import speech_recognition as sr

def speech_to_text():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Capture audio from the user
    with sr.Microphone() as source:
        print("Say something:")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Convert audio to text
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    text = speech_to_text()
    if text:
        print("You said:", text)






def display_word_videos(sentence, folder_path):
    # Tokenize the input sentence into words
    words = sentence.split()
    
    # Create a list to store the video widgets
    video_widgets = []
    
    for word in words:
        # Check if a .webp file exists for the word
        image_path = os.path.join(folder_path, f"{word}.webp")
        
        if os.path.exists(image_path):
            # Create video widget for each image
            with open(image_path, "rb") as f:
                video_data = f.read()
            video_widget = widgets.Image(value=video_data, format='webp', width=600, height=600)
            video_widgets.append(video_widget)
        else:
            print(f"No image found for '{word}'")

    # Create a container widget to display the video widgets
    container = widgets.VBox(video_widgets)
    display(container)

# Example usage
#sentence = input("Enter a sentence: ")
sentence = text
folder_path = r'C:\Users\vidit shrama\Downloads\filtered_data' # Change this to the path of your image folder
display_word_videos(sentence, folder_path)
