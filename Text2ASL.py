import os
import ipywidgets as widgets
from IPython.display import display, HTML
import time

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
sentence = input("Enter a sentence: ")
folder_path = r'C:\Users\vidit shrama\Downloads\filtered_data' # Change this to the path of your image folder
display_word_videos(sentence, folder_path)
